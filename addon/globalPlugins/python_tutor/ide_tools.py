# -*- coding: utf-8 -*-
# ============================================================================
# Módulo: globalPlugins/python_tutor/ide_tools.py
# Propósito: Herramientas profesionales de desarrollo accesible tipo VS Code:
#            IntelliSense, Depurador paso a paso, Gestor de Intérpretes/Venv,
#            Ejecutor de Pruebas Unitarias, Formateador PEP 8 y Refactorización.
# Autor: Kevin Andrés Velasquez Vargas
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
    import ui
    import speech
except ImportError:
    ui = None
    speech = None

from .audio_manager import SoundManager
from .progress import ProgressManager

# Documentación concisa y accesible para autocompletado y Shift+F1
DOCS_PYTHON = {
    "print": "print(*objects, sep=' ', end='\\n'): Imprime objetos en la consola de salida.",
    "input": "input(prompt=''): Lee una línea de texto introducida por el usuario.",
    "len": "len(s): Devuelve el número de elementos de una secuencia o colección.",
    "range": "range(stop) o range(start, stop, step): Genera una secuencia inmutable de números.",
    "str": "str(object=''): Convierte un objeto a su representación en cadena de texto.",
    "int": "int(x=0): Convierte un número o cadena a un número entero.",
    "float": "float(x=0.0): Convierte un número o cadena a número decimal de coma flotante.",
    "bool": "bool(x=False): Devuelve True o False según el valor de verdad del argumento.",
    "list": "list(iterable=()): Crea una lista mutable de elementos ordenados.",
    "dict": "dict(**kwargs): Crea una colección mutable de pares clave-valor.",
    "set": "set(iterable=()): Crea un conjunto mutable de elementos únicos sin orden.",
    "tuple": "tuple(iterable=()): Crea una tupla inmutable de elementos ordenados.",
    "open": "open(file, mode='r', encoding=None): Abre un archivo y devuelve un objeto de flujo.",
    "type": "type(object): Devuelve el tipo del objeto especificado.",
    "sum": "sum(iterable, start=0): Suma todos los elementos de un iterable numérico.",
    "min": "min(iterable): Devuelve el elemento menor de una colección.",
    "max": "max(iterable): Devuelve el elemento mayor de una colección.",
    "abs": "abs(x): Devuelve el valor absoluto de un número.",
    "round": "round(number, ndigits=None): Redondea un número al número de decimales indicado.",
    "enumerate": "enumerate(iterable, start=0): Devuelve tuplas con índice y elemento.",
    "zip": "zip(*iterables): Agrupa elementos correspondientes de múltiples iterables.",
    "isinstance": "isinstance(object, classinfo): Comprueba si un objeto es instancia de una clase.",
    "append": "lista.append(elemento): Agrega un nuevo elemento al final de la lista.",
    "extend": "lista.extend(iterable): Extiende la lista agregando todos los elementos del iterable.",
    "insert": "lista.insert(indice, elemento): Inserta un elemento en la posición indicada.",
    "pop": "lista.pop([indice]): Quita y devuelve el elemento en el índice (por defecto el último).",
    "remove": "lista.remove(valor): Elimina la primera aparición del valor en la lista.",
    "sort": "lista.sort(key=None, reverse=False): Ordena los elementos de la lista en su lugar.",
    "reverse": "lista.reverse(): Invierte el orden de los elementos de la lista en su lugar.",
    "keys": "diccionario.keys(): Devuelve una vista de todas las claves del diccionario.",
    "values": "diccionario.values(): Devuelve una vista de todos los valores del diccionario.",
    "items": "diccionario.items(): Devuelve una vista de pares (clave, valor) del diccionario.",
    "get": "diccionario.get(clave, default=None): Devuelve el valor de la clave si existe.",
    "update": "diccionario.update(otro): Actualiza el diccionario con pares clave-valor de otro.",
    "split": "cadena.split(sep=None): Divide la cadena en una lista de subcadenas según el separador.",
    "join": "separador.join(iterable): Concatena los elementos de un iterable con el separador.",
    "strip": "cadena.strip(): Elimina espacios en blanco al inicio y al final de la cadena.",
    "lower": "cadena.lower(): Devuelve una copia de la cadena en minúsculas.",
    "upper": "cadena.upper(): Devuelve una copia de la cadena en mayúsculas.",
    "replace": "cadena.replace(viejo, nuevo): Reemplaza apariciones de una subcadena por otra.",
    "startswith": "cadena.startswith(prefijo): Devuelve True si la cadena comienza con el prefijo.",
    "endswith": "cadena.endswith(sufijo): Devuelve True si la cadena termina con el sufijo.",
    "def": "def nombre(parametros): Declara una función definida por el usuario.",
    "return": "return [expresion]: Termina la ejecución de una función y devuelve un resultado.",
    "if": "if condicion: Ejecuta un bloque de código si la condición es verdadera.",
    "elif": "elif condicion: Rama condicional alternativa tras un if o elif anterior.",
    "else": "else: Bloque que se ejecuta si ninguna condición previa fue verdadera.",
    "for": "for variable in secuencia: Itera sobre los elementos de una colección o rango.",
    "while": "while condicion: Repite un bloque de código mientras la condición sea verdadera.",
    "try": "try: Inicia un bloque vigilado para capturar posibles excepciones en tiempo de ejecución.",
    "except": "except [TipoError]: Maneja una excepción producida dentro del bloque try.",
    "finally": "finally: Bloque que se ejecuta siempre al finalizar el try, haya o no excepción.",
    "class": "class NombreClase: Declara una nueva clase para programación orientada a objetos.",
    "import": "import modulo: Importa un módulo para utilizar sus funciones y clases.",
    "from": "from modulo import objeto: Importa elementos específicos directamente al espacio de nombres.",
    "True": "True: Valor booleano verdadero (1).",
    "False": "False: Valor booleano falso (0).",
    "None": "None: Objeto especial que representa la ausencia de valor o valor nulo.",
    "break": "break: Interrumpe y sale inmediatamente del bucle actual for o while.",
    "continue": "continue: Salta a la siguiente iteración del bucle actual.",
    "pass": "pass: Instrucción nula que no hace nada, usada como marcador de posición.",
    "self": "self: Primer parámetro convencional en métodos de instancia que referencia al objeto actual."
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

    return f"Símbolo: {nombre}. Sin documentación adicional disponible."


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
        return codigo, "El editor está vacío. No hay código para formatear."

    # Validar sintaxis previa
    try:
        ast.parse(codigo)
    except SyntaxError as e:
        return codigo, f"No se puede formatear debido a un error de sintaxis en la línea {e.lineno}: {e.msg}"

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
        return codigo, "El formateo fue cancelado para preservar la integridad del código."

    return codigo_resultado, f"Código formateado según PEP 8. Se ajustaron {ajustes} líneas."


class AutoCompleteDialog(wx.Dialog):
    """Diálogo accesible de autocompletado inteligente con previsualización de documentación."""
    def __init__(self, parent, prefijo, opciones):
        super(AutoCompleteDialog, self).__init__(parent, title="Sugerencias de Autocompletado", size=(580, 420))
        self.prefijo = prefijo
        self.opciones = opciones
        self.seleccion = ""

        panel = wx.Panel(self, style=wx.TAB_TRAVERSAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        lbl = wx.StaticText(panel, label=f"Sugerencias para '{prefijo}':")
        vbox.Add(lbl, flag=wx.LEFT | wx.TOP | wx.RIGHT, border=12)

        self.list_box = wx.ListBox(panel, choices=self.opciones)
        self.list_box.SetName("Lista de sugerencias de autocompletado.")
        if self.opciones:
            self.list_box.SetSelection(0)
        vbox.Add(self.list_box, proportion=2, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=12)

        lbl_doc = wx.StaticText(panel, label="Documentación:")
        vbox.Add(lbl_doc, flag=wx.LEFT | wx.TOP | wx.RIGHT, border=12)

        self.txt_doc = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2)
        self.txt_doc.SetName("Documentación de la sugerencia seleccionada.")
        vbox.Add(self.txt_doc, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=12)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        btn_insertar = wx.Button(panel, wx.ID_OK, label="Insertar")
        btn_insertar.SetDefault()
        btn_cancelar = wx.Button(panel, wx.ID_CANCEL, label="Cancelar")
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
        super(RenameSymbolDialog, self).__init__(parent, title="Renombrar Símbolo", size=(480, 220))
        self.simbolo_actual = simbolo_actual
        self.nuevo_nombre = ""

        panel = wx.Panel(self, style=wx.TAB_TRAVERSAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        lbl = wx.StaticText(panel, label=f"Renombrar '{simbolo_actual}' por:")
        vbox.Add(lbl, flag=wx.LEFT | wx.TOP | wx.RIGHT, border=12)

        self.txt_nuevo = wx.TextCtrl(panel, value=simbolo_actual)
        self.txt_nuevo.SetName("Nuevo nombre del símbolo")
        self.txt_nuevo.SelectAll()
        vbox.Add(self.txt_nuevo, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=12)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        btn_ok = wx.Button(panel, wx.ID_OK, label="Renombrar")
        btn_ok.SetDefault()
        btn_cancel = wx.Button(panel, wx.ID_CANCEL, label="Cancelar")
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
                ui.message("El nombre del símbolo no puede estar vacío.")
            return
        if not val.isidentifier():
            msg = f"'{val}' no es un identificador válido de Python."
            if ui:
                ui.message(msg)
            wx.MessageBox(msg, "Identificador no válido", wx.OK | wx.ICON_WARNING, self)
            return
        self.nuevo_nombre = val
        self.EndModal(wx.ID_OK)


class ExtractFunctionDialog(wx.Dialog):
    """Diálogo accesible para extraer código seleccionado a una nueva función."""
    def __init__(self, parent):
        super(ExtractFunctionDialog, self).__init__(parent, title="Extraer a Función", size=(480, 220))
        self.nombre_funcion = ""

        panel = wx.Panel(self, style=wx.TAB_TRAVERSAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        lbl = wx.StaticText(panel, label="Nombre de la nueva función:")
        vbox.Add(lbl, flag=wx.LEFT | wx.TOP | wx.RIGHT, border=12)

        self.txt_nombre = wx.TextCtrl(panel, value="nueva_funcion")
        self.txt_nombre.SetName("Nombre de la nueva función")
        self.txt_nombre.SelectAll()
        vbox.Add(self.txt_nombre, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=12)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        btn_ok = wx.Button(panel, wx.ID_OK, label="Extraer")
        btn_ok.SetDefault()
        btn_cancel = wx.Button(panel, wx.ID_CANCEL, label="Cancelar")
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
            msg = f"'{val}' no es un identificador válido para una función."
            if ui:
                ui.message(msg)
            wx.MessageBox(msg, "Nombre no válido", wx.OK | wx.ICON_WARNING, self)
            return
        self.nombre_funcion = val
        self.EndModal(wx.ID_OK)


class StepDebuggerDialog(wx.Dialog):
    """Diálogo accesible para la depuración interactiva paso a paso de scripts."""
    def __init__(self, parent, codigo, breakpoints=None):
        super(StepDebuggerDialog, self).__init__(parent, title="Depurador Interactivo Paso a Paso", size=(720, 560))
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

        self.lbl_estado = wx.StaticText(panel, label="Iniciando depurador...")
        font = self.lbl_estado.GetFont()
        font.SetWeight(wx.FONTWEIGHT_BOLD)
        self.lbl_estado.SetFont(font)
        vbox.Add(self.lbl_estado, flag=wx.LEFT | wx.TOP | wx.RIGHT, border=12)

        lbl_vars = wx.StaticText(panel, label="Variables locales activas:")
        vbox.Add(lbl_vars, flag=wx.LEFT | wx.TOP | wx.RIGHT, border=12)

        self.txt_vars = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2)
        self.txt_vars.SetName("Variables locales activas")
        vbox.Add(self.txt_vars, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=12)

        lbl_sal = wx.StaticText(panel, label="Salida de consola:")
        vbox.Add(lbl_sal, flag=wx.LEFT | wx.TOP | wx.RIGHT, border=12)

        self.txt_salida = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2)
        self.txt_salida.SetName("Salida de consola del depurador")
        vbox.Add(self.txt_salida, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=12)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.btn_paso = wx.Button(panel, label="Paso Siguiente (F10)")
        self.btn_paso.SetDefault()
        self.btn_continuar = wx.Button(panel, label="Continuar (F5)")
        self.btn_detener = wx.Button(panel, wx.ID_CANCEL, label="Detener (Escape)")

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
            self.lbl_estado.SetLabel("No hay líneas ejecutables en el código.")
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
            marca_bp = "Punto de interrupción, " if es_bp else ""
            msg = f"{marca_bp}Línea {linea_num}: {codigo_linea}"
            self.lbl_estado.SetLabel(msg)
            if speech and hasattr(speech, 'speakMessage'):
                speech.speakMessage(msg)
            if ui:
                ui.message(msg)
        else:
            msg = "Depuración finalizada. Se ejecutaron todas las líneas."
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
            salida_err = f"Error en la línea {linea_num}: {e}"
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
            vars_txt = "(Sin variables declaradas aún)"
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
        super(TestRunnerDialog, self).__init__(parent, title="Ejecutor de Pruebas Unitarias", size=(680, 520))
        self.codigo = codigo

        panel = wx.Panel(self, style=wx.TAB_TRAVERSAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        self.lbl_resumen = wx.StaticText(panel, label="Ejecutando pruebas...")
        font = self.lbl_resumen.GetFont()
        font.SetWeight(wx.FONTWEIGHT_BOLD)
        self.lbl_resumen.SetFont(font)
        vbox.Add(self.lbl_resumen, flag=wx.LEFT | wx.TOP | wx.RIGHT, border=12)

        self.txt_detalles = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2)
        self.txt_detalles.SetName("Detalles de resultados de las pruebas unitarias")
        vbox.Add(self.txt_detalles, proportion=1, flag=wx.EXPAND | wx.ALL, border=12)

        btn_cerrar = wx.Button(panel, wx.ID_OK, label="Cerrar")
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
            msg = "El editor está vacío. Escribe pruebas unitarias antes de ejecutar."
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
            resumen = f"Fallo al cargar el script: {e}"
            self.lbl_resumen.SetLabel("Error en la ejecución del script")
            self.txt_detalles.SetValue(resumen)
            if speech and hasattr(speech, 'speakMessage'):
                speech.speakMessage(resumen)
            if ui:
                ui.message(resumen)
            return

        test_cases = [obj for obj in scope.values() if isinstance(obj, type) and issubclass(obj, unittest.TestCase)]

        if not test_cases:
            mensaje = (
                "No se encontraron clases heredadas de unittest.TestCase en el código.\n\n"
                "Para escribir pruebas unitarias accesibles, estructura tu script de esta forma:\n\n"
                "import unittest\n\n"
                "class PruebasEjemplo(unittest.TestCase):\n"
                "    def test_suma(self):\n"
                "        self.assertEqual(2 + 2, 4)\n\n"
                "if __name__ == '__main__':\n"
                "    unittest.main()\n"
            )
            self.lbl_resumen.SetLabel("Sin clases de prueba unittest")
            self.txt_detalles.SetValue(mensaje)
            if speech and hasattr(speech, 'speakMessage'):
                speech.speakMessage("No se detectaron clases de prueba unittest en el editor.")
            if ui:
                ui.message("No se detectaron clases de prueba unittest.")
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
            resumen = f"Todas las pruebas superadas. Total: {total}, Exitosas: {exitosas}."
            if SoundManager:
                SoundManager.play('exito')
        else:
            resumen = f"Pruebas finalizadas con fallos. Total: {total}, Fallos: {fallos}, Errores: {errores}."
            if SoundManager:
                SoundManager.play('error')

        self.lbl_resumen.SetLabel(resumen)
        self.txt_detalles.SetValue(f"{resumen}\n\nDetalles del ejecutor:\n{stream.getvalue()}")

        if speech and hasattr(speech, 'speakMessage'):
            speech.speakMessage(resumen)
        if ui:
            ui.message(resumen)


class InterpreterManagerDialog(wx.Dialog):
    """Diálogo accesible para gestionar y seleccionar el intérprete de Python o entorno virtual."""
    def __init__(self, parent):
        super(InterpreterManagerDialog, self).__init__(parent, title="Gestor de Intérpretes y Entornos Virtuales", size=(680, 440))
        self.parent = parent
        self.interpretes_detectados = self.detectar_interpretes()

        prog = ProgressManager.load_progress()
        self.interprete_guardado = prog.get("custom_python_path", sys.executable)

        panel = wx.Panel(self, style=wx.TAB_TRAVERSAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        lbl = wx.StaticText(panel, label="Selecciona el entorno de Python para ejecutar scripts:")
        vbox.Add(lbl, flag=wx.LEFT | wx.TOP | wx.RIGHT, border=12)

        opciones_txt = [f"{desc}: {path}" for desc, path in self.interpretes_detectados]
        self.list_box = wx.ListBox(panel, choices=opciones_txt)
        self.list_box.SetName("Lista de intérpretes detectados")

        # Seleccionar el guardado si coincide
        sel_idx = 0
        for i, (desc, path) in enumerate(self.interpretes_detectados):
            if path.lower() == self.interprete_guardado.lower():
                sel_idx = i
                break
        self.list_box.SetSelection(sel_idx)
        vbox.Add(self.list_box, proportion=1, flag=wx.EXPAND | wx.ALL, border=12)

        hbox_btn = wx.BoxSizer(wx.HORIZONTAL)
        btn_examinar = wx.Button(panel, label="Examinar otro python.exe...")
        btn_aplicar = wx.Button(panel, wx.ID_OK, label="Establecer como activo")
        btn_aplicar.SetDefault()
        btn_cancelar = wx.Button(panel, wx.ID_CANCEL, label="Cancelar")

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
        encontrados.append(("Python integrado de NVDA", sys.executable))

        # 2. Python del sistema en PATH
        py_system = shutil.which("python")
        if py_system and py_system.lower() != sys.executable.lower():
            encontrados.append(("Python del sistema (PATH)", py_system))

        py3_system = shutil.which("python3")
        if py3_system and py3_system.lower() != sys.executable.lower() and py3_system != py_system:
            encontrados.append(("Python 3 del sistema", py3_system))

        # 3. Entornos virtuales en el directorio actual o carpetas típicas
        dirs_base = [os.getcwd(), os.path.dirname(os.path.abspath(__file__))]
        nombres_venv = [".venv", "venv", "env"]
        for base in dirs_base:
            for nv in nombres_venv:
                cand = os.path.join(base, nv, "Scripts", "python.exe")
                if os.path.isfile(cand) and cand.lower() not in [p.lower() for _, p in encontrados]:
                    encontrados.append((f"Entorno virtual ({nv})", cand))

        return encontrados

    def on_examinar(self, event=None):
        dlg = wx.FileDialog(
            self,
            message="Seleccionar ejecutable de Python",
            wildcard="Ejecutable de Python (python.exe)|python.exe|Todos los archivos (*.*)|*.*",
            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
        )
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            self.interpretes_detectados.append(("Entorno personalizado", path))
            idx = self.list_box.Append(f"Entorno personalizado: {path}")
            self.list_box.SetSelection(idx)
        dlg.Destroy()

    def on_aplicar(self, event=None):
        sel = self.list_box.GetSelection()
        if sel != wx.NOT_FOUND:
            desc, path = self.interpretes_detectados[sel]
            ProgressManager.set_setting("custom_python_path", path)
            msg = f"Intérprete activo establecido: {desc}"
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
