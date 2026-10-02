# -*- coding: utf-8 -*-
# ============================================================================
# Módulo: globalPlugins/python_tutor/ide_tools.py
# Propósito: Herramientas profesionales de desarrollo accesible tipo VS Code:
#            IntelliSense, Depurador paso a paso, Gestor de Intérpretes/Venv,
#            Ejecutor de Pruebas Unitarias, Formateador PEP 8 y Refactorización.
# Autor: Kevin Andrés Velasquez Vargas
# Internacionalización (i18n): MisterK-Dev (desarrollado con Google Antigravity 2.0)
# Licencia: GNU General Public License v3.0 (GPLv3)
# ============================================================================

import os
import sys
import re
import ast
import io
import unittest
import shutil
import wx

try:
    import addonHandler
    addonHandler.initTranslation()
except Exception:
    pass

try:
    _
except NameError:
    import gettext
    _loc = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "locale")
    try:
        _t = gettext.translation("nvda", localedir=_loc, languages=["es"])
        _ = _t.gettext
    except Exception:
        def _(msg):
            return msg

try:
    import ui
    import speech
except ImportError:
    ui = None
    speech = None

from .audio_manager import SoundManager
from .progress import ProgressManager

# Documentación concisa y accesible para autocompletado y Shift+F1
DOCS_PYTHON = {
    "print": _("print(*objects, sep=' ', end='\\n'): Prints objects to the output console."),
    "input": _("input(prompt=''): Reads a line of text entered by the user."),
    "len": _("len(s): Returns the number of items in a sequence or collection."),
    "range": _("range(stop) or range(start, stop, step): Generates an immutable sequence of numbers."),
    "str": _("str(object=''): Converts an object to its string representation."),
    "int": _("int(x=0): Converts a number or string to an integer."),
    "float": _("float(x=0.0): Converts a number or string to a floating-point decimal number."),
    "bool": _("bool(x=False): Returns True or False based on the truth value of the argument."),
    "list": _("list(iterable=()): Creates a mutable list of ordered items."),
    "dict": _("dict(**kwargs): Creates a mutable collection of key-value pairs."),
    "set": _("set(iterable=()): Creates a mutable set of unique unordered items."),
    "tuple": _("tuple(iterable=()): Creates an immutable tuple of ordered items."),
    "open": _("open(file, mode='r', encoding=None): Opens a file and returns a stream object."),
    "type": _("type(object): Returns the type of the specified object."),
    "sum": _("sum(iterable, start=0): Sums all elements of a numerical iterable."),
    "min": _("min(iterable): Returns the smallest item in a collection."),
    "max": _("max(iterable): Returns the largest item in a collection."),
    "abs": _("abs(x): Returns the absolute value of a number."),
    "round": _("round(number, ndigits=None): Rounds a number to the given number of decimal places."),
    "enumerate": _("enumerate(iterable, start=0): Returns tuples with index and item."),
    "zip": _("zip(*iterables): Groups corresponding elements from multiple iterables."),
    "isinstance": _("isinstance(object, classinfo): Checks if an object is an instance of a class."),
    "append": _("list.append(item): Adds a new item to the end of the list."),
    "extend": _("list.extend(iterable): Extends the list by appending all items from the iterable."),
    "insert": _("list.insert(index, item): Inserts an item at the specified position."),
    "pop": _("list.pop([index]): Removes and returns the item at index (default last)."),
    "remove": _("list.remove(value): Removes the first occurrence of the value from the list."),
    "sort": _("list.sort(key=None, reverse=False): Sorts the items of the list in place."),
    "reverse": _("list.reverse(): Reverses the order of the items of the list in place."),
    "keys": _("dict.keys(): Returns a view of all dictionary keys."),
    "values": _("dict.values(): Returns a view of all dictionary values."),
    "items": _("dict.items(): Returns a view of dictionary (key, value) pairs."),
    "get": _("dict.get(key, default=None): Returns the value of key if it exists."),
    "update": _("dict.update(other): Updates the dictionary with key-value pairs from another."),
    "split": _("string.split(sep=None): Splits the string into a list of substrings by separator."),
    "join": _("separator.join(iterable): Concatenates elements of an iterable with the separator."),
    "strip": _("string.strip(): Removes leading and trailing whitespace from the string."),
    "lower": _("string.lower(): Returns a copy of the string in lowercase."),
    "upper": _("string.upper(): Returns a copy of the string in uppercase."),
    "replace": _("string.replace(old, new): Replaces occurrences of a substring with another."),
    "startswith": _("string.startswith(prefix): Returns True if the string starts with the prefix."),
    "endswith": _("string.endswith(suffix): Returns True if the string ends with the suffix."),
    "def": _("def name(parameters): Declares a user-defined function."),
    "return": _("return [expression]: Ends function execution and returns a result."),
    "if": _("if condition: Executes a block of code if the condition is true."),
    "elif": _("elif condition: Alternative conditional branch after an earlier if or elif."),
    "else": _("else: Block executed if no previous condition was true."),
    "for": _("for variable in sequence: Iterates over items of a collection or range."),
    "while": _("while condition: Repeats a block of code while condition is true."),
    "try": _("try: Starts a guarded block to catch potential runtime exceptions."),
    "except": _("except [TypeError]: Handles an exception raised inside the try block."),
    "finally": _("finally: Block that always executes upon finishing try, whether exception occurred or not."),
    "class": _("class ClassName: Declares a new class for object-oriented programming."),
    "import": _("import module: Imports a module to use its functions and classes."),
    "from": _("from module import object: Imports specific items directly into namespace."),
    "True": _("True: Boolean true value (1)."),
    "False": _("False: Boolean false value (0)."),
    "None": _("None: Special object representing the absence of a value or null value."),
    "break": _("break: Immediately interrupts and exits the current for or while loop."),
    "continue": _("continue: Skips to the next iteration of the current loop."),
    "pass": _("pass: Null statement that does nothing, used as a placeholder."),
    "self": _("self: Conventional first parameter in instance methods referencing the current object.")
}


def obtener_documentacion_simbolo(nombre):
    """Devuelve la explicación accesible de un símbolo o función."""
    if not nombre:
        return ""
    nombre = nombre.strip()
    if nombre in DOCS_PYTHON:
        return DOCS_PYTHON[nombre]

    # Intentar obtener docstring de builtins de Python
    try:
        import builtins
        if hasattr(builtins, nombre):
            obj = getattr(builtins, nombre)
            doc = getattr(obj, '__doc__', '')
            if doc:
                primera_linea = doc.strip().split('\n')[0]
                return f"{nombre}: {primera_linea}"
    except Exception:
        pass

    # Translators: Fallback message when no documentation is available for a symbol. {name} is the symbol name.
    return _("Symbol: {name}. No additional documentation available.").format(name=nombre)


def formatear_codigo_pep8(codigo):
    """
    Formatea código Python siguiendo las pautas de estilo PEP 8:
    - Normaliza la sangría a 4 espacios exactos.
    - Normaliza espacios alrededor de operadores binarios (=, ==, !=, +, -, *, /, etc.).
    - Añade un espacio tras comas y dos puntos.
    - Elimina espacios en blanco redundantes al final de cada línea.
    - Asegura un salto de línea final.
    Verifica que la sintaxis no se altere usando el módulo ast.
    """
    if not codigo.strip():
        return codigo, _("The editor is empty. There is no code to format.")

    # Validar sintaxis previa
    try:
        ast.parse(codigo)
    except SyntaxError as e:
        # Translators: Error message when PEP 8 formatting fails due to a syntax error. {line} is the line number, {msg} is the syntax error message.
        return codigo, _("Cannot format due to a syntax error on line {line}: {msg}").format(line=e.lineno, msg=e.msg)

    lineas = codigo.splitlines()
    nuevas_lineas = []
    ajustes = 0

    operadores_binarios = [
        (re.compile(r'([^=<>!+\-*/%&|^~])\s*(==|!=|<=|>=|\+=|-=|\*=|/=|%=)\s*([^=])'), r'\1 \2 \3'),
        (re.compile(r'([^=<>!+\-*/%&|^~])\s*=\s*([^=])'), r'\1 = \2'),
        (re.compile(r'([a-zA-Z0-9_\)\]])\s*(\+|\-|\*|\/|\/\/|\%)\s*([a-zA-Z0-9_\(\[])'), r'\1 \2 \3'),
        (re.compile(r',\s*'), ', '),
        (re.compile(r':\s*#'), ': #')
    ]

    for linea in lineas:
        linea_original = linea
        # 1. Quitar espacios finales
        linea_rstrip = linea.rstrip()
        if not linea_rstrip:
            nuevas_lineas.append("")
            continue

        # 2. Medir sangría inicial y normalizar tabs a 4 espacios
        indent_len = len(linea_rstrip) - len(linea_rstrip.lstrip(' \t'))
        chars_indent = linea_rstrip[:indent_len].replace('\t', '    ')
        contenido = linea_rstrip[indent_len:]

        # Normalizar nivel de sangría al múltiplo de 4 más cercano si está desfasado
        nivel = (len(chars_indent) + 2) // 4
        sangria_normal = '    ' * nivel

        # 3. Normalizar espacios en operadores solo si no es comentario puro ni cadena multilínea
        if not contenido.startswith('#'):
            for regex, rep in operadores_binarios:
                contenido = regex.sub(rep, contenido)

        linea_formateada = sangria_normal + contenido
        if linea_formateada != linea_original:
            ajustes += 1
        nuevas_lineas.append(linea_formateada)

    codigo_resultado = '\n'.join(nuevas_lineas) + '\n'

    # Validar que el código formateado sigue siendo sintácticamente idéntico
    try:
        ast.parse(codigo_resultado)
    except Exception:
        return codigo, _("Formatting was cancelled to preserve code integrity.")

    # Translators: Success message for PEP 8 formatter. {count} is the number of adjusted lines.
    return codigo_resultado, _("Code formatted according to PEP 8. {count} lines adjusted.").format(count=ajustes)


class AutoCompleteDialog(wx.Dialog):
    """Diálogo accesible de autocompletado inteligente con previsualización de documentación."""
    def __init__(self, parent, prefijo, opciones):
        super(AutoCompleteDialog, self).__init__(parent, title=_("Autocomplete Suggestions"), size=(580, 420))
        self.prefijo = prefijo
        self.opciones = opciones
        self.seleccion = ""

        panel = wx.Panel(self, style=wx.TAB_TRAVERSAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Translators: Label for autocomplete suggestions dialog. {prefix} is the current typed prefix.
        lbl = wx.StaticText(panel, label=_("Suggestions for '{prefix}':").format(prefix=prefijo))
        vbox.Add(lbl, flag=wx.LEFT | wx.TOP | wx.RIGHT, border=12)

        self.list_box = wx.ListBox(panel, choices=self.opciones)
        self.list_box.SetName(_("Autocomplete suggestions list."))
        if self.opciones:
            self.list_box.SetSelection(0)
        vbox.Add(self.list_box, proportion=2, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=12)

        lbl_doc = wx.StaticText(panel, label=_("Documentation:"))
        vbox.Add(lbl_doc, flag=wx.LEFT | wx.TOP | wx.RIGHT, border=12)

        self.txt_doc = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2)
        self.txt_doc.SetName(_("Documentation of the selected suggestion."))
        vbox.Add(self.txt_doc, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=12)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        btn_insertar = wx.Button(panel, wx.ID_OK, label=_("Insert"))
        btn_insertar.SetDefault()
        btn_cancelar = wx.Button(panel, wx.ID_CANCEL, label=_("Cancel"))
        hbox.Add(btn_insertar, flag=wx.RIGHT, border=8)
        hbox.Add(btn_cancelar)
        vbox.Add(hbox, flag=wx.ALIGN_CENTER | wx.ALL, border=12)

        panel.SetSizer(vbox)

        self.Bind(wx.EVT_CHAR_HOOK, self.on_char_hook)
        btn_insertar.Bind(wx.EVT_BUTTON, self.on_insertar)
        self.list_box.Bind(wx.EVT_LISTBOX, self.on_cambio_seleccion)
        self.list_box.Bind(wx.EVT_LISTBOX_DCLICK, self.on_insertar)

        self.actualizar_doc()
        self.CenterOnParent()
        self.list_box.SetFocus()

    def on_cambio_seleccion(self, event=None):
        self.actualizar_doc()

    def actualizar_doc(self):
        sel = self.list_box.GetSelection()
        if sel != wx.NOT_FOUND:
            item = self.opciones[sel]
            doc = obtener_documentacion_simbolo(item)
            self.txt_doc.SetValue(doc)
            if speech and hasattr(speech, 'speakMessage'):
                speech.speakMessage(f"{item}, {doc}")

    def on_char_hook(self, event):
        keycode = event.GetKeyCode()
        if keycode == wx.WXK_ESCAPE:
            self.EndModal(wx.ID_CANCEL)
        elif keycode in (wx.WXK_RETURN, wx.WXK_NUMPAD_ENTER):
            self.on_insertar(None)
        else:
            event.Skip()

    def on_insertar(self, event=None):
        sel = self.list_box.GetSelection()
        if sel != wx.NOT_FOUND:
            self.seleccion = self.opciones[sel]
            self.EndModal(wx.ID_OK)
        else:
            self.EndModal(wx.ID_CANCEL)


class RenameSymbolDialog(wx.Dialog):
    """Diálogo accesible para renombrar un símbolo en todo el archivo."""
    def __init__(self, parent, simbolo_actual):
        super(RenameSymbolDialog, self).__init__(parent, title=_("Rename Symbol"), size=(480, 220))
        self.simbolo_actual = simbolo_actual
        self.nuevo_nombre = ""

        panel = wx.Panel(self, style=wx.TAB_TRAVERSAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Translators: Label for renaming symbol dialog. {symbol} is the current symbol name.
        lbl = wx.StaticText(panel, label=_("Rename '{symbol}' to:").format(symbol=simbolo_actual))
        vbox.Add(lbl, flag=wx.LEFT | wx.TOP | wx.RIGHT, border=12)

        self.txt_nuevo = wx.TextCtrl(panel, value=simbolo_actual)
        self.txt_nuevo.SetName(_("New symbol name"))
        self.txt_nuevo.SelectAll()
        vbox.Add(self.txt_nuevo, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=12)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        btn_ok = wx.Button(panel, wx.ID_OK, label=_("Rename"))
        btn_ok.SetDefault()
        btn_cancel = wx.Button(panel, wx.ID_CANCEL, label=_("Cancel"))
        hbox.Add(btn_ok, flag=wx.RIGHT, border=8)
        hbox.Add(btn_cancel)
        vbox.Add(hbox, flag=wx.ALIGN_CENTER | wx.ALL, border=12)

        panel.SetSizer(vbox)
        self.Bind(wx.EVT_CHAR_HOOK, self.on_char_hook)
        btn_ok.Bind(wx.EVT_BUTTON, self.on_ok)
        self.CenterOnParent()
        self.txt_nuevo.SetFocus()

    def on_char_hook(self, event):
        if event.GetKeyCode() == wx.WXK_ESCAPE:
            self.EndModal(wx.ID_CANCEL)
        elif event.GetKeyCode() in (wx.WXK_RETURN, wx.WXK_NUMPAD_ENTER):
            self.on_ok(None)
        else:
            event.Skip()

    def on_ok(self, event=None):
        val = self.txt_nuevo.GetValue().strip()
        if not val:
            if ui:
                ui.message(_("Symbol name cannot be empty."))
            return
        if not val.isidentifier():
            # Translators: Error when symbol name is not a valid Python identifier. {name} is the invalid name.
            msg = _("'{name}' is not a valid Python identifier.").format(name=val)
            if ui:
                ui.message(msg)
            wx.MessageBox(msg, _("Invalid identifier"), wx.OK | wx.ICON_WARNING, self)
            return
        self.nuevo_nombre = val
        self.EndModal(wx.ID_OK)


class ExtractFunctionDialog(wx.Dialog):
    """Diálogo accesible para extraer código seleccionado a una nueva función."""
    def __init__(self, parent):
        super(ExtractFunctionDialog, self).__init__(parent, title=_("Extract to Function"), size=(480, 220))
        self.nombre_funcion = ""

        panel = wx.Panel(self, style=wx.TAB_TRAVERSAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        lbl = wx.StaticText(panel, label=_("New function name:"))
        vbox.Add(lbl, flag=wx.LEFT | wx.TOP | wx.RIGHT, border=12)

        self.txt_nombre = wx.TextCtrl(panel, value=_("new_function"))
        self.txt_nombre.SetName(_("New function name"))
        self.txt_nombre.SelectAll()
        vbox.Add(self.txt_nombre, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=12)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        btn_ok = wx.Button(panel, wx.ID_OK, label=_("Extract"))
        btn_ok.SetDefault()
        btn_cancel = wx.Button(panel, wx.ID_CANCEL, label=_("Cancel"))
        hbox.Add(btn_ok, flag=wx.RIGHT, border=8)
        hbox.Add(btn_cancel)
        vbox.Add(hbox, flag=wx.ALIGN_CENTER | wx.ALL, border=12)

        panel.SetSizer(vbox)
        self.Bind(wx.EVT_CHAR_HOOK, self.on_char_hook)
        btn_ok.Bind(wx.EVT_BUTTON, self.on_ok)
        self.CenterOnParent()
        self.txt_nombre.SetFocus()

    def on_char_hook(self, event):
        if event.GetKeyCode() == wx.WXK_ESCAPE:
            self.EndModal(wx.ID_CANCEL)
        elif event.GetKeyCode() in (wx.WXK_RETURN, wx.WXK_NUMPAD_ENTER):
            self.on_ok(None)
        else:
            event.Skip()

    def on_ok(self, event=None):
        val = self.txt_nombre.GetValue().strip()
        if not val or not val.isidentifier():
            # Translators: Error when function name is not a valid Python identifier. {name} is the invalid name.
            msg = _("'{name}' is not a valid function identifier.").format(name=val)
            if ui:
                ui.message(msg)
            wx.MessageBox(msg, _("Invalid name"), wx.OK | wx.ICON_WARNING, self)
            return
        self.nombre_funcion = val
        self.EndModal(wx.ID_OK)


class StepDebuggerDialog(wx.Dialog):
    """Diálogo accesible para la depuración interactiva paso a paso de scripts."""
    def __init__(self, parent, codigo, breakpoints=None):
        super(StepDebuggerDialog, self).__init__(parent, title=_("Interactive Step-by-Step Debugger"), size=(720, 560))
        self.codigo = codigo
        self.lineas = codigo.splitlines()
        self.breakpoints = breakpoints or set()
        self.linea_actual_idx = 0
        self.locales = {}
        self.salida_acumulada = []
        self.detenido = False

        # Filtrar líneas no vacías y no comentarios para la ejecución
        self.lineas_ejecutables = []
        for i, l in enumerate(self.lineas):
            s = l.strip()
            if s and not s.startswith('#'):
                self.lineas_ejecutables.append(i)

        panel = wx.Panel(self, style=wx.TAB_TRAVERSAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        self.lbl_estado = wx.StaticText(panel, label=_("Starting debugger..."))
        font = self.lbl_estado.GetFont()
        font.SetWeight(wx.FONTWEIGHT_BOLD)
        self.lbl_estado.SetFont(font)
        vbox.Add(self.lbl_estado, flag=wx.LEFT | wx.TOP | wx.RIGHT, border=12)

        lbl_vars = wx.StaticText(panel, label=_("Active local variables:"))
        vbox.Add(lbl_vars, flag=wx.LEFT | wx.TOP | wx.RIGHT, border=12)

        self.txt_vars = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2)
        self.txt_vars.SetName(_("Active local variables"))
        vbox.Add(self.txt_vars, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=12)

        lbl_sal = wx.StaticText(panel, label=_("Console output:"))
        vbox.Add(lbl_sal, flag=wx.LEFT | wx.TOP | wx.RIGHT, border=12)

        self.txt_salida = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2)
        self.txt_salida.SetName(_("Debugger console output"))
        vbox.Add(self.txt_salida, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=12)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.btn_paso = wx.Button(panel, label=_("Next Step (F10)"))
        self.btn_paso.SetDefault()
        self.btn_continuar = wx.Button(panel, label=_("Continue (F5)"))
        self.btn_detener = wx.Button(panel, wx.ID_CANCEL, label=_("Stop (Escape)"))

        hbox.Add(self.btn_paso, flag=wx.RIGHT, border=8)
        hbox.Add(self.btn_continuar, flag=wx.RIGHT, border=8)
        hbox.Add(self.btn_detener)
        vbox.Add(hbox, flag=wx.ALIGN_CENTER | wx.ALL, border=12)

        panel.SetSizer(vbox)

        self.Bind(wx.EVT_CHAR_HOOK, self.on_char_hook)
        self.btn_paso.Bind(wx.EVT_BUTTON, self.on_paso)
        self.btn_continuar.Bind(wx.EVT_BUTTON, self.on_continuar)

        self.CenterOnParent()
        self.posicionar_inicio()
        self.btn_paso.SetFocus()

    def posicionar_inicio(self):
        if not self.lineas_ejecutables:
            self.lbl_estado.SetLabel(_("There are no executable lines in the code."))
            self.btn_paso.Disable()
            self.btn_continuar.Disable()
            return

        self.idx_ejecutable = 0
        self.anunciar_linea_actual()

    def anunciar_linea_actual(self):
        if self.idx_ejecutable < len(self.lineas_ejecutables):
            linea_num = self.lineas_ejecutables[self.idx_ejecutable] + 1
            codigo_linea = self.lineas[linea_num - 1].strip()
            es_bp = (linea_num in self.breakpoints)
            marca_bp = _("Breakpoint, ") if es_bp else ""
            # Translators: Announcement of current line in debugger. {breakpoint} is breakpoint alert if set, {line} is line number, {code} is code content.
            msg = _("{breakpoint}Line {line}: {code}").format(breakpoint=marca_bp, line=linea_num, code=codigo_linea)
            self.lbl_estado.SetLabel(msg)
            if speech and hasattr(speech, 'speakMessage'):
                speech.speakMessage(msg)
            if ui:
                ui.message(msg)
        else:
            msg = _("Debugging finished. All lines were executed.")
            self.lbl_estado.SetLabel(msg)
            self.btn_paso.Disable()
            self.btn_continuar.Disable()
            if speech and hasattr(speech, 'speakMessage'):
                speech.speakMessage(msg)
            if ui:
                ui.message(msg)

    def on_paso(self, event=None):
        if self.idx_ejecutable >= len(self.lineas_ejecutables):
            return

        linea_num = self.lineas_ejecutables[self.idx_ejecutable] + 1
        lineas_hasta_aqui = self.lineas[:linea_num]
        codigo_acumulado = '\n'.join(lineas_hasta_aqui)

        # Ejecutar de forma segura capturando stdout
        buffer_salida = io.StringIO()
        old_stdout = sys.stdout
        try:
            sys.stdout = buffer_salida
            exec_scope = {}
            exec(codigo_acumulado, exec_scope)
            self.locales = {k: v for k, v in exec_scope.items() if not k.startswith('__')}
        except Exception as e:
            # Translators: Error during debugger step execution. {line} is line number, {error} is exception message.
            salida_err = _("Error on line {line}: {error}").format(line=linea_num, error=e)
            self.salida_acumulada.append(salida_err)
            self.txt_salida.SetValue('\n'.join(self.salida_acumulada))
            if speech and hasattr(speech, 'speakMessage'):
                speech.speakMessage(salida_err)
            if ui:
                ui.message(salida_err)
            self.btn_paso.Disable()
            self.btn_continuar.Disable()
            return
        finally:
            sys.stdout = old_stdout

        sal = buffer_salida.getvalue().strip()
        if sal:
            self.txt_salida.SetValue(sal)

        # Mostrar variables
        if self.locales:
            vars_txt = "\n".join(f"{k} = {repr(v)}" for k, v in self.locales.items())
        else:
            vars_txt = _("(No variables declared yet)")
        self.txt_vars.SetValue(vars_txt)

        self.idx_ejecutable += 1
        self.anunciar_linea_actual()

    def on_continuar(self, event=None):
        while self.idx_ejecutable < len(self.lineas_ejecutables):
            linea_num = self.lineas_ejecutables[self.idx_ejecutable] + 1
            if linea_num in self.breakpoints and self.idx_ejecutable > 0:
                self.anunciar_linea_actual()
                return
            self.on_paso(None)

    def on_char_hook(self, event):
        keycode = event.GetKeyCode()
        if keycode == wx.WXK_ESCAPE:
            self.EndModal(wx.ID_CANCEL)
        elif keycode == wx.WXK_F10:
            self.on_paso(None)
        elif keycode == wx.WXK_F5:
            self.on_continuar(None)
        else:
            event.Skip()


class TestRunnerDialog(wx.Dialog):
    """Diálogo accesible para ejecutar pruebas unitarias con reporte estructurado."""
    def __init__(self, parent, codigo):
        super(TestRunnerDialog, self).__init__(parent, title=_("Unit Test Runner"), size=(680, 520))
        self.codigo = codigo

        panel = wx.Panel(self, style=wx.TAB_TRAVERSAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        self.lbl_resumen = wx.StaticText(panel, label=_("Running tests..."))
        font = self.lbl_resumen.GetFont()
        font.SetWeight(wx.FONTWEIGHT_BOLD)
        self.lbl_resumen.SetFont(font)
        vbox.Add(self.lbl_resumen, flag=wx.LEFT | wx.TOP | wx.RIGHT, border=12)

        self.txt_detalles = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2)
        self.txt_detalles.SetName(_("Unit test results details"))
        vbox.Add(self.txt_detalles, proportion=1, flag=wx.EXPAND | wx.ALL, border=12)

        btn_cerrar = wx.Button(panel, wx.ID_OK, label=_("Close"))
        btn_cerrar.SetDefault()
        vbox.Add(btn_cerrar, flag=wx.ALIGN_CENTER | wx.BOTTOM, border=12)

        panel.SetSizer(vbox)
        self.Bind(wx.EVT_CHAR_HOOK, self.on_char_hook)
        self.CenterOnParent()
        btn_cerrar.SetFocus()

        wx.CallAfter(self.ejecutar_pruebas)

    def on_char_hook(self, event):
        if event.GetKeyCode() == wx.WXK_ESCAPE:
            self.EndModal(wx.ID_CANCEL)
        else:
            event.Skip()

    def ejecutar_pruebas(self):
        if not self.codigo.strip():
            msg = _("The editor is empty. Write unit tests before running.")
            self.lbl_resumen.SetLabel(msg)
            self.txt_detalles.SetValue(msg)
            if speech and hasattr(speech, 'speakMessage'):
                speech.speakMessage(msg)
            if ui:
                ui.message(msg)
            return

        # Comprobar si hay TestCase en el script
        scope = {}
        buffer_salida = io.StringIO()
        try:
            exec(self.codigo, scope)
        except Exception as e:
            # Translators: Error message when executing unit test script fails to load. {error} is the error message.
            resumen = _("Failed to load script: {error}").format(error=e)
            self.lbl_resumen.SetLabel(_("Error in script execution"))
            self.txt_detalles.SetValue(resumen)
            if speech and hasattr(speech, 'speakMessage'):
                speech.speakMessage(resumen)
            if ui:
                ui.message(resumen)
            return

        test_cases = [obj for obj in scope.values() if isinstance(obj, type) and issubclass(obj, unittest.TestCase)]

        if not test_cases:
            mensaje = _(
                "No classes inheriting from unittest.TestCase were found in the code.\n\n"
                "To write accessible unit tests, structure your script like this:\n\n"
                "import unittest\n\n"
                "class ExampleTests(unittest.TestCase):\n"
                "    def test_sum(self):\n"
                "        self.assertEqual(2 + 2, 4)\n\n"
                "if __name__ == '__main__':\n"
                "    unittest.main()\n"
            )
            self.lbl_resumen.SetLabel(_("No unittest test classes"))
            self.txt_detalles.SetValue(mensaje)
            if speech and hasattr(speech, 'speakMessage'):
                speech.speakMessage(_("No unittest test classes were detected in the editor."))
            if ui:
                ui.message(_("No unittest test classes were detected."))
            return

        suite = unittest.TestSuite()
        loader = unittest.TestLoader()
        for tc in test_cases:
            suite.addTests(loader.loadTestsFromTestCase(tc))

        stream = io.StringIO()
        runner = unittest.TextTestRunner(stream=stream, verbosity=2)
        resultado = runner.run(suite)

        total = resultado.testsRun
        fallos = len(resultado.failures)
        errores = len(resultado.errors)
        exitosas = total - fallos - errores

        if resultado.wasSuccessful():
            # Translators: Unit test success summary. {total} is total tests run, {passed} is passed tests.
            resumen = _("All tests passed. Total: {total}, Passed: {passed}.").format(total=total, passed=exitosas)
            if SoundManager:
                SoundManager.play('exito')
        else:
            # Translators: Unit test failure summary. {total} is total tests run, {failures} is failed tests, {errors} is errored tests.
            resumen = _("Tests finished with failures. Total: {total}, Failures: {failures}, Errors: {errors}.").format(total=total, failures=fallos, errors=errores)
            if SoundManager:
                SoundManager.play('error')

        self.lbl_resumen.SetLabel(resumen)
        # Translators: Details output format for unit test runner. {summary} is summary line, {details} is test output stream.
        self.txt_detalles.SetValue(_("{summary}\n\nRunner details:\n{details}").format(summary=resumen, details=stream.getvalue()))

        if speech and hasattr(speech, 'speakMessage'):
            speech.speakMessage(resumen)
        if ui:
            ui.message(resumen)


class InterpreterManagerDialog(wx.Dialog):
    """Diálogo accesible para gestionar y seleccionar el intérprete de Python o entorno virtual."""
    def __init__(self, parent):
        super(InterpreterManagerDialog, self).__init__(parent, title=_("Interpreter and Virtual Environment Manager"), size=(680, 440))
        self.parent = parent
        self.interpretes_detectados = self.detectar_interpretes()

        prog = ProgressManager.load_progress()
        self.interprete_guardado = prog.get("custom_python_path", sys.executable)

        panel = wx.Panel(self, style=wx.TAB_TRAVERSAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        lbl = wx.StaticText(panel, label=_("Select the Python environment to run scripts:"))
        vbox.Add(lbl, flag=wx.LEFT | wx.TOP | wx.RIGHT, border=12)

        opciones_txt = [f"{desc}: {path}" for desc, path in self.interpretes_detectados]
        self.list_box = wx.ListBox(panel, choices=opciones_txt)
        self.list_box.SetName(_("List of detected interpreters"))

        # Seleccionar el guardado si coincide
        sel_idx = 0
        for i, (desc, path) in enumerate(self.interpretes_detectados):
            if path.lower() == self.interprete_guardado.lower():
                sel_idx = i
                break
        self.list_box.SetSelection(sel_idx)
        vbox.Add(self.list_box, proportion=1, flag=wx.EXPAND | wx.ALL, border=12)

        hbox_btn = wx.BoxSizer(wx.HORIZONTAL)
        btn_examinar = wx.Button(panel, label=_("Browse for another python.exe..."))
        btn_aplicar = wx.Button(panel, wx.ID_OK, label=_("Set as active"))
        btn_aplicar.SetDefault()
        btn_cancelar = wx.Button(panel, wx.ID_CANCEL, label=_("Cancel"))

        hbox_btn.Add(btn_examinar, flag=wx.RIGHT, border=8)
        hbox_btn.Add(btn_aplicar, flag=wx.RIGHT, border=8)
        hbox_btn.Add(btn_cancelar)
        vbox.Add(hbox_btn, flag=wx.ALIGN_CENTER | wx.BOTTOM, border=12)

        panel.SetSizer(vbox)

        self.Bind(wx.EVT_CHAR_HOOK, self.on_char_hook)
        btn_examinar.Bind(wx.EVT_BUTTON, self.on_examinar)
        btn_aplicar.Bind(wx.EVT_BUTTON, self.on_aplicar)
        self.list_box.Bind(wx.EVT_LISTBOX_DCLICK, self.on_aplicar)

        self.CenterOnParent()
        self.list_box.SetFocus()

    def detectar_interpretes(self):
        encontrados = []
        # 1. Intérprete actual de NVDA / Python en ejecución
        encontrados.append((_("Embedded NVDA Python"), sys.executable))

        # 2. Python del sistema en PATH
        py_system = shutil.which("python")
        if py_system and py_system.lower() != sys.executable.lower():
            encontrados.append((_("System Python (PATH)"), py_system))

        py3_system = shutil.which("python3")
        if py3_system and py3_system.lower() != sys.executable.lower() and py3_system != py_system:
            encontrados.append((_("System Python 3"), py3_system))

        # 3. Entornos virtuales en el directorio actual o carpetas típicas
        dirs_base = [os.getcwd(), os.path.dirname(os.path.abspath(__file__))]
        nombres_venv = [".venv", "venv", "env"]
        for base in dirs_base:
            for nv in nombres_venv:
                cand = os.path.join(base, nv, "Scripts", "python.exe")
                if os.path.isfile(cand) and cand.lower() not in [p.lower() for _, p in encontrados]:
                    # Translators: Label for virtual environment. {env} is directory name (e.g. .venv, venv).
                    encontrados.append((_("Virtual environment ({env})").format(env=nv), cand))

        return encontrados

    def on_examinar(self, event=None):
        dlg = wx.FileDialog(
            self,
            message=_("Select Python executable"),
            wildcard=_("Python Executable (python.exe)|python.exe|All files (*.*)|*.*"),
            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
        )
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            desc_custom = _("Custom environment")
            self.interpretes_detectados.append((desc_custom, path))
            # Translators: List entry for custom environment. {path} is interpreter file path.
            idx = self.list_box.Append(_("Custom environment: {path}").format(path=path))
            self.list_box.SetSelection(idx)
        dlg.Destroy()

    def on_aplicar(self, event=None):
        sel = self.list_box.GetSelection()
        if sel != wx.NOT_FOUND:
            desc, path = self.interpretes_detectados[sel]
            ProgressManager.set_setting("custom_python_path", path)
            # Translators: Confirmation of active Python interpreter. {desc} is interpreter description.
            msg = _("Active interpreter set: {desc}").format(desc=desc)
            if speech and hasattr(speech, 'speakMessage'):
                speech.speakMessage(msg)
            if ui:
                ui.message(msg)
            self.EndModal(wx.ID_OK)
        else:
            self.EndModal(wx.ID_CANCEL)

    def on_char_hook(self, event):
        if event.GetKeyCode() == wx.WXK_ESCAPE:
            self.EndModal(wx.ID_CANCEL)
        else:
            event.Skip()
