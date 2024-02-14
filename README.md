# Compiler Starter Project

- [Compiler Starter Project](#compiler-starter-project)
  - [Dependencies](#dependencies)
  - [To use](#to-use)
    - [Run on Docker (preferred)](#run-on-docker-preferred)
    - [Run on Local Machine](#run-on-local-machine)
  - [Code Explain](#code-explain)
  - [GUI](#gui)


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

## GUI

We use `PyQt6` and `qt designer 6` for GUI.
You can start to learn this tool from [here](https://www.pythonguis.com/tutorials/pyqt6-first-steps-qt-designer/#:~:text=To%20load%20.,a%20fully%2Dfunctional%20PyQt6%20object).

To launch `QT designer`, use `pipenv run pyqt6-tools designer`

