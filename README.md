# pyBagPlot
Python package to display live readouts of ventilator data

To install on an Ubuntu 20.04 machine:

```bash
sudo apt install python3-pip
python3 -m pip install --user --upgrade pip poetry git+https://github.com/VentilatorsInPeoria/pyBagPlot.git
pybagplot
```

To update to the latest version of the master branch code:

```bash
python3 -m pip install --user --upgrade git+https://github.com/VentilatorsInPeoria/pyBagPlot.git@master
```

To uninstall on an Ubuntu 20.04 machine:

```bash
python3 -m pip uninstall pybagplot
```

To develop on an Ubuntu 20.04 machine:

```bash
sudo apt install python3-pip python3-venv
python3 -m pip install --user --upgrade pip poetry
git clone https://github.com/VentilatorsInPeoria/pyBagPlot.git
cd pyBagPlot/
python3 -m venv .venv
source .venv/bin/activate
# The install command will need to be re-run if changes are made to pyproject.toml
poetry install
# Make code changes here as needed
# Changes made to Python code will be re-read each execution
pybagplot
deactivate
```

To quickly validate code changes before making a commit (from within an activated venv, pwd is python source code dir):

```bash
flake8
```

To do a full validation before pushing your commit (need not be in a venv, pwd is python source code dir):

```bash
tox
```