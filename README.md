# Compiler Starter Project

- [Compiler Starter Project](#compiler-starter-project)
  - [Dependencies](#dependencies)
  - [To use](#to-use)
    - [Run on Docker (preferred)](#run-on-docker-preferred)
    - [Run on Local Machine](#run-on-local-machine)
  - [Code Explain](#code-explain)
    - [components/lexica.py](#componentslexicapy)
    - [components/parsers.py](#componentsparserspy)
      - [MyParser class](#myparser-class)
      - [ASTParser class](#astparser-class)
    - [components/memory.py](#componentsmemorypy)
    - [main.py and components/main.ui](#mainpy-and-componentsmainui)
  - [Design a GUI](#design-a-gui)


This is the starter project for the Programming Language and Compiler course @ AIT. 
Since 2024, we have used `Python`.

## Dependencies
- Python version 3.9.18
- `sly` as a submodule [link](https://github.com/dabeaz/sly)
- `PyQt6` for GUI development

## To use

I designed this project to run on a `Docker` container. 
However, if you are not a `Docker` enthusiast like me, you can still run this project locally.

### Run on Docker (preferred)

Once you install `Docker` in your system, you can do the following.

1. (Optional) Click `Use this template` on the top right of this page to clone this to your repository.
2. Clone the project to your local machine.
3. Clone submodule with this `git submodule update --init --recursive`.
4. (Optional) Install X11Client if you want to use GUI in docker. 
   - For `Windows`: [X410](https://x410.dev) is the best but you will need to pay. 
   - For `Mac`: [XQuartz](https://www.xquartz.org) is the one I used. 
   - For `Linux`/`Ubuntu`: You can simply map `DISPLAY`. No additional app is needed.
5. Run `docker compose up -d --build` to build and run the container.
6. Use `VSCode` to dev the project remotely.

### Run on Local Machine

This might not work because I have never tried this on my machine.
But, generally, it should be as follows.

1. (Optional) Click `Use this template` on the top right of this page to clone this to your repository.
2. Clone the project to your local machine.
3. Clone submodule with this `git submodule update --init --recursive`.
4. Set `PYTHONPATH` to include `/path/to/sly`.
5. Run `pipenv install` inside `src/`.
6. You might also need to install `PyQt6` separately.


## Code Explain

Inside `src/` folder is all the code developed.

```txt
src/
  |- components/
      |- ast/
          |- statement.py
      |- lexica.py
      |- main.ui
      |- memory.py
      |- parsers.py
  |- main.py
  |- Pipfile
  |- Pipfile.lock
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


### main.py and components/main.ui

Finally, the `main.py` is the main file to run the entire project.
It will render a GUI from `components/main.ui` that was designed from `PyQt6`.
This shows how to bind a function with a button and how to display the result back to the GUI.

## Design a GUI

We use `PyQt6` and `qt designer 6` for GUI.
You can start to learn this tool from [here](https://www.pythonguis.com/tutorials/pyqt6-first-steps-qt-designer/#:~:text=To%20load%20.,a%20fully%2Dfunctional%20PyQt6%20object).

To launch `QT designer`, use `pipenv run pyqt6-tools designer` and to open the existing UI use `pipenv run pyqt6-tools designer <path/to/file.ui>`