# Compiler Starter Project

- [Compiler Starter Project](#compiler-starter-project)
  - [Dependencies](#dependencies)
  - [Getting Started](#getting-started)
    - [VSCode setup](#vscode-setup)
    - [Running Debug](#running-debug)
    - [Running `Task`](#running-task)
    - [Installing dependency](#installing-dependency)
  - [Code Explain](#code-explain)
    - [components/lexica.py](#componentslexicapy)
    - [components/parsers.py](#componentsparserspy)
      - [MyParser class](#myparser-class)
      - [ASTParser class](#astparser-class)
    - [components/memory.py](#componentsmemorypy)
    - [`main.py` and `components/main.ui`](#mainpy-and-componentsmainui)
  - [Design a GUI](#design-a-gui)

This is the starter project for the Programming Language and Compiler course @ AIT.
Since 2024, we use `Python`.

## Dependencies

- Python version 3.9.18
- [`uv`](https://docs.astral.sh/uv/getting-started/installation/) for managing project
- `PySide6` for GUI development

## Getting Started

As of January 2026, this project drop the support for `Docker`.
We figure that it only make thing more complicated and decided to use `uv` and `vscode` to control the environment.

To use this repository, follow below steps.

1. (Optional) Click `Use this template` on the top right of this page to clone this to your repository.
2. Clone the project to your local machine.
3. Go to project folder and run `uv sync`.

### VSCode setup

The repository has a file `.vscode/extensions.json` which will automatically install extension for you.
In case that this mechanism fails, here are the list of required extension.

- `ms-python.python`
- `ms-python.debugpy`

### Running Debug

The repository has support for running the code in debug mode.
Check the `.vscode/launch.json`.

By default, you can run `[example] Python Debugger` option which launch the `src/example` module.
We sort-of giving an example of how to create mulitple entrypoints by providing the second option `[project] Python Debugger` which is not ready to use until you create a module `src/project`.

### Running `Task`

To execute the module, we provide `Tasks` under the `.vscode/tasks.json`.
There are three tasks initially.

1. **start app**: For launching the `example` project.
2. **start designer**: For launching `PySide6-designer` app.
3. **compile designer**: For compiling the `ui` file generated from the `PySide6-designer`.

To run them, you can do it from the command palette <kbd>Ctrl/Cmd</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>.
Choose `Tasks: Run Task`, and choose the option will appear.

### Installing dependency

Most of the requirement should be sorted out with `uv sync`.
However, for no obvious reason right now, `PySide6-designer` would not run within the `uv` context.
You will need to install the `PySide6` library again using `pip install`.

```sh
pip install pyside6
```

When you are done with this project, you can remove them with this

```sh
pip uninstall pyside6 PySide6_Addons PySide6_Essentials
```

## Code Explain

Inside `src/example/` folder is all the code developed.

```txt
compiler-starter-project/
  |- components/
      |- ast/
          |- statement.py
      |- lexica.py
      |- main.ui
      |- memory.py
      |- parsers.py
  |- main.py
```

Since the project is done just to showcase libraries and techniques, here we divided it into subsections to explain the code.

### components/lexica.py

This file showcases the Lexica analyzer component. It has a `MyLexer` class that extends `sly.Lexer`.
It will translate a code/string into `token` stream/generator that feeds to a `Parser`.
This file has a main just for testing the class.

### components/parsers.py

There are two parsers.
(1) `MyParser` and (2) `ASTParser`.

#### MyParser class

This class is what I call immediate evaluation which each of the semantics, once reduced, evaluates/calculates right away.
This type of parser is fine for calculator projects or simple parsing.
This parser also implements [`Memory`](#componentsmemorypy) and `Variable assignment`.

#### ASTParser class

This is a more complex but flexible way of parsing.
[AST (Abstract Syntax Trees)](https://en.wikipedia.org/wiki/Abstract_syntax_tree) is actually a parse tree.
This will allow you to control when to run a subsection of code like `if-else` statement.
You can see that the semantic part is only creating an object inside `components.ast`.
All the logic (in this case, addition and subtraction) is in the AST object.
The Parser is there is create a parse tree that once ready will execute `.run()`.
I only add the essentials to demonstrate this technique.

### components/memory.py

This contains `Memory` class which is a singleton.
Inside is just a simple dictionary where `variable_name` is a key and `{'value':value,'data_type':<type>}` as a value.
Whether this solution is appropriate or not is your judgment.

### `main.py` and `components/main.ui`

Finally, the `main.py` is the main file to run the entire project.
It will render a GUI from `components/main.ui` that was designed from `PyQt6`.
This shows how to bind a function with a button and how to display the result back to the GUI.

## Design a GUI

We use `PySide6` and `pyside6-designer` for GUI development.
You can start to learn this tool from 

- [Official Document](https://doc.qt.io/qtforpython-6/tools/pyside-designer.html)
- [3rd party Tutorial](https://www.pythonguis.com/tutorials/pyside6-first-steps-qt-designer/)

To launch the designer, use [Running `Task`](#running-task)
