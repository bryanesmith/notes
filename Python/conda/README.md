# conda and Anaconda

* `conda` is package & environment manager (similar to `virtualenv` and `pyenv`); **Anaconda** is distribution that includes conda, Python, and >150 scientific packages
* Unlike pip, conda is *not* Python-specific
* Not all Python packages available in conda; you'll use pip, too

# Commands

## Environments
| Command | Description |
| ------- | ----------- |
| `conda env list` | List environments |
| `conda create -n <env-name> python=<python-version> anaconda` | Create environment |
| `source activate <env-name>` | Use environment |
| `conda install -n <env-name> <package-name>` | Install package in environment |
| `source deactivate` | Deactivate current environment |
| `conda remove -n yourenvname -all` | Remove an environment |

## Packages
| Command | Description |
| ------- | ----------- |
| `conda install numpy=1.10 scipy panda` | Install package(s) in root environment |
| `conda update <package>` | Update specific package. Note `upgrade` is an alias. |
| `conda remove <package>` | Remove package(s) |
| `conda list` | List installed packages |
| `conda update conda && conda update --all` | Update all packages in default environment |
| `conda search *beautifulsoup*` | Search for package |

# Resources
* [Conda cheet sheet](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)
