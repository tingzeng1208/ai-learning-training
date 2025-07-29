use uv to manage python package and project
100x faster
to install, either powershell or pip install uv


uv python list: list all available python versions
uv run main.py: run main.py in python
uv run --python 3.9.21 main.py: use python 3.9.21 to run main.py
uv python install 3.8: install python 3.8
uv python uninstall 3.8: unintall 3.8
uv run --with rich --python 3.14 main.py


uv init (in project dirjhhj): to start a project with basic template files

uv remove a package
uv add a package

uv sync: to sync the package in .toml with .venv 