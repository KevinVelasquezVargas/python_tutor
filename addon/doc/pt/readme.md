# Aprendizagem de Python com NVDA [![Versão](https://img.shields.io/badge/Vers%C3%A3o-3.1.0-blue.svg)](https://github.com/KevinVelasquezVargas/python_tutor/releases/latest) [![Compatibilidade](https://img.shields.io/badge/NVDA-2022.1%20a%202026.2-brightgreen.svg)](https://www.nvaccess.org/) [![Licença](https://img.shields.io/badge/Licen%C3%A7a-GPLv3-blue.svg)](LICENSE)

Ambiente acessível de desenvolvimento e formação para a aprendizagem de Python com o leitor de ecrã NVDA. Estruturado num plano formativo de 40 capítulos e numa modalidade dupla que combina um tutor interativo com um editor autónomo sem barreiras visuais.

## Conteúdo

1. [Instalação](#instalação)
2. [Funcionalidades Principais](#funcionalidades-principais)
3. [Atalhos de Teclado](#atalhos-de-teclado)
4. [Plano Formativo](#plano-formativo)
5. [Configuração](#configuração)
6. [Adicionar um Novo Idioma de Lições](#adicionar-um-novo-idioma-de-lições)
7. [Testes Automatizados](#testes-automatizados)
8. [Suporte e Colaboração](#suporte-e-colaboração)
9. [Licença](#licença)

---

## Instalação

1. Descarregue o pacote oficial mais recente da secção de [Lançamentos (Releases)](https://github.com/KevinVelasquezVargas/python_tutor/releases/latest).
2. Abra o ficheiro descarregado (`.nvda-addon`) para que o gestor de complementos do NVDA inicie o processo.
3. Confirme a instalação e reinicie o leitor de ecrã.
4. Prima `NVDA + Control + Shift + P` para iniciar a aplicação.

---

## Funcionalidades Principais

* **Plano pedagógico orientado:** 40 capítulos e 190 lições distribuídos por 9 módulos sequenciais. Introduz fundamentos conceptuais antes de abordar a sintaxe formal.
* **Modalidade dupla de trabalho:** Alternância imediata (`Control + M`) entre o modo orientado com retroalimentação automática e um editor autónomo limpo para projetos pessoais.
* **Interface adaptativa:** Ocultação automática do editor e da consola em lições teóricas e avaliações conceptuais mediante seletores acessíveis (`wx.RadioBox`).
* **Arquitetura nativa:** Utilização exclusiva de módulos da biblioteca padrão de Python (`sqlite3`, `json`, `math`, `random`, `datetime`, `urllib`), eliminando dependências externas e riscos de compilação.
* **Sinais acústicos tiflotécnicos:** Sonificação para níveis de indentação PEP 8, diagnóstico de delimitadores e validação de sintaxe.
* **Assistência pedagógica:** Explicador de código local sem ligação (`F1`) e suporte opcional para consultas avançadas com a API do Google Gemini (`Control + Shift + I`).
* **Suporte multilingue ampliável:** Espanhol, Inglês e Português incluídos oficialmente. Adicionar um idioma novo não exige tocar em Python: basta acrescentar um catálogo JSON de lições (consulte [Adicionar um Novo Idioma de Lições](#adicionar-um-novo-idioma-de-lições)).

---

## Atalhos de Teclado

| Atalho | Categoria | Ação |
| :--- | :--- | :--- |
| `NVDA + Ctrl + Shift + P` | Global | Abrir ou focar o ambiente |
| `Ctrl + M` | Modos | Alternar entre Modo Tutor e Modo Editor Autónomo |
| `Ctrl + Enter` / `Ctrl + E` | Execução | Executar código e verificar o desafio |
| `F5` | Execução | Executar o script atual |
| `Alt + Seta Direita` | Navegação | Avançar para o passo seguinte |
| `Alt + Seta Esquerda` | Navegação | Recuar para o passo anterior |
| `F3` / `Ctrl + I` | Tutor | Verbalizar a instrução pedagógica ativa |
| `Ctrl + P` | Tutor | Pedir pista escalonada |
| `F1` | Tutor | Explicação local da linha atual |
| `Shift + F1` | Referência | Documentação técnica do símbolo sob o cursor |
| `Ctrl + R` | Tutor | Restaurar o código de partida |
| `Ctrl + 1` | Tutor | Seletor de capítulos e progresso |
| `Ctrl + J` | Ferramentas | Abrir consola interativa REPL |
| `Ctrl + Shift + I` | Ferramentas | Consultar assistente com IA (API Gemini) |
| `F6` | Navegação | Alternar foco entre editor e consola |
| `Ctrl + 4` | Navegação | Colocar o foco no editor |
| `Ctrl + 5` | Navegação | Colocar o foco na consola |
| `Ctrl + 6` | Consola | Ler a última linha emitida |
| `Ctrl + Shift + C` | Consola | Ler toda a saída acumulada |
| `Ctrl + L` | Edição | Anunciar linha e coluna atuais |
| `Ctrl + N` | Ficheiro | Criar novo ficheiro |
| `Ctrl + O` | Ficheiro | Abrir ficheiro `.py` |
| `Ctrl + S` | Ficheiro | Guardar alterações |
| `Ctrl + Shift + S` | Ficheiro | Guardar como |
| `Ctrl + F` | Edição | Procurar texto |
| `Ctrl + G` | Edição | Ir para um número de linha |
| `Ctrl + Espaço` | Edição | Autocompletar acessível |
| `Shift + Alt + F` | Edição | Formatar documento segundo PEP 8 |
| `Ctrl + /` / `Ctrl + K` | Edição | Alternar comentário de linha (`#`) |
| `Ctrl + D` | Edição | Duplicar linha ativa |
| `Ctrl + Shift + K` | Edição | Eliminar linha ativa |
| `Ctrl + Shift + R` | Refatoração | Extrair seleção para nova função |
| `F2` | Refatoração | Renomear identificador |
| `Ctrl + Shift + O` | Estrutura | Lista acessível de funções e classes |
| `Alt + N` / `Alt + P` | Estrutura | Saltar para o cabeçalho seguinte / anterior |
| `F7` | Diagnóstico | Validar sintaxe e balanceamento de delimitadores |
| `F4` | Diagnóstico | Saltar para a linha do erro do Traceback |
| `F9` | Depuração | Alternar ponto de interrupção |
| `F10` | Depuração | Depuração interativa passo a passo |
| `Ctrl + T` | Testes | Executar testes unitários |
| `Ctrl + Shift + P` | Ambiente | Gestor de intérpretes e ambientes virtuais |
| `Ctrl + Shift + E` | Ferramentas | Explorador acessível de ficheiros e projetos |
| `F11` | Ajuda | Diálogo acessível de atalhos de teclado |
| `F12` | Ajuda | Documentação completa no navegador |
| `Escape` | Geral | Fechar a caixa de diálogo ativa |

---

## Plano Formativo

| Módulo | Capítulos | Conteúdo |
| :--- | :--- | :--- |
| **0. Fundamentos de Computação** | 1 a 5 | Arquitetura, sistema binário, CPU, leitores de ecrã e pensamento algorítmico. |
| **1. Saída, Memória e Variáveis** | 6 a 9 | Saída padrão com `print()`, atribuição dinâmica e PEP 8. |
| **2. Tipos Fundamentais e Interação** | 10 a 14 | Tipos `int`, `float`, `str`, interpolação com f-strings e captura com `input()`. |
| **3. Lógica Booleana e Controlo** | 15 a 19 | Expressões booleanas, conectores lógicos e condicionais `if`, `else`, `elif`. |
| **4. Ciclos e Automatização** | 20 a 23 | Ciclos `for` com `range()`, ciclos `while`, controlo de execução e diretivas de fluxo. |
| **5. Estruturas de Dados** | 24 a 28 | Listas indexadas, operações de mutação, iteração, tuplos e dicionários. |
| **6. Modularidade e Exceções** | 29 a 32 | Funções com `def`, retorno com `return`, âmbito e gestão de falhas (`try`/`except`). |
| **7. Persistência e Objetos (POO)** | 33 a 36 | Manuseamento seguro de ficheiros (`with open`), JSON, classes, instâncias e métodos. |
| **8. Biblioteca Padrão e Projeto** | 37 a 40 | Módulos `math`, `random`, `datetime`, bases de dados `sqlite3` e projeto final integrador. |

---

## Configuração

Caminho de acesso: **Menu NVDA > Preferências > Opções > Aprendizagem de Python com NVDA**

* **Modo de arranque:** Modo Aprendizagem Orientada ou Modo Editor Autónomo.
* **Sinais acústicos:** Ativação da sonificação de indentação PEP 8 e alertas.
* **Modo da tecla F1:** Explicação local sem ligação ou consulta com a IA.
* **Chave API do Gemini:** Configuração opcional para consultas de IA.

O idioma do ambiente é detetado automaticamente a partir do idioma do NVDA (variantes como `pt_BR` ou `en_US` são normalizadas para o catálogo disponível) e pode ser mudado a quente em qualquer momento a partir do menu **Ajuda > Mudar idioma** da janela do tutor.

---

## Adicionar um Novo Idioma de Lições

Os currículos traduzidos vivem em catálogos JSON independentes do código (`addon/locale/<idioma>/lessons.json`), junto com o resto da localização do complemento. Ao recompilar, o idioma novo aparece automaticamente na deteção automática do idioma do NVDA (variantes como `pt_BR` ou `en_US` são normalizadas para o catálogo disponível) e no menu *Mudar idioma*.

1. Gere o catálogo base em espanhol a partir do código fonte:

   ```bash
   uv run python tools/extract_lessons.py
   ```

2. Copie `addon/locale/es/lessons.json` para `addon/locale/<idioma>/lessons.json` (por exemplo, `addon/locale/fr/lessons.json`) e traduza os valores. As chaves permanecem em espanhol. A tradução pode ser parcial (capítulo a capítulo): tudo o que faltar será mostrado em espanhol como recurso.

   O glossário técnico segue o mesmo mecanismo: copie `addon/locale/es/glossary.json` para `addon/locale/<idioma>/glossary.json` e traduza as definições; os termos que faltarem serão mostrados em espanhol e também pode acrescentar termos novos editando o JSON.

3. Respeite estas regras nos desafios de código (os validadores vivem em `curriculum.py` e nunca são traduzidos):
   * `salida_esperada`: deve permanecer byte-idêntica ao original.
   * `codigo`: só os comentários `#` são traduzidos; os literais de cadeia devem coincidir exatamente com o original.
   * `opciones`: conserve a ordem das opções (a resposta correta é validada por posição) e traduza cada opção completa.

4. Interface do complemento (opcional, mas recomendado), mediante gettext oficial:
   * Gere o modelo e crie o catálogo do idioma (requer gettext no PATH):

     ```bash
     scons pot
     msginit -i python_tutor.pot -o addon/locale/<idioma>/LC_MESSAGES/nvda.po
     ```

     (ou copie `addon/locale/es/LC_MESSAGES/nvda.po`, já alinhado com o modelo).
   * Preencha os `msgstr` (os `msgid` permanecem em espanhol, o idioma base) e recompile com `scons`: os ficheiros `.mo`, o manifesto traduzido e a documentação HTML são gerados automaticamente.
   * Traduza também `addon/doc/<idioma>/readme.md` (a documentação que abre com `F12`); o `scons` gera o HTML correspondente de forma automática.

5. Recompile e verifique:

   ```bash
   scons
   python -m unittest tests/test_tutor.py
   ```

---

## Testes Automatizados

O projeto implementa testes unitários baseados em `unittest` para verificar o correto funcionamento do editor e a integridade das lições:

```bash
python -m unittest tests/test_tutor.py
```

---

## Suporte e Colaboração

* **Reporte de problemas:** [Gestor de incidentes no GitHub](https://github.com/KevinVelasquezVargas/python_tutor/issues)
* **Contacto direto:** [kevinvelasquezvargas@gmail.com](mailto:kevinvelasquezvargas@gmail.com)
* **Patrocínio:** [Donativos voluntários via PayPal](https://paypal.me/kevinvelasquezvargas)

---

## Licença

Este projeto está abrangido pela Licença Pública Geral GNU v3.0 (GPLv3). Consulte o ficheiro [LICENSE](LICENSE) para mais detalhes.

**Autor:** Kevin Andrés Velasquez Vargas.
