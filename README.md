# Pipenv Cookiecutter
[![License](https://img.shields.io/github/license/jevandezande/pipenv-cookiecutter)](https://github.com/jevandezande/pipenv-cookiecutter/blob/master/LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/jevandezande/pipenv-cookiecutter/Test)](https://github.com/jevandezande/pipenv-cookiecutter/actions/)
[![Codecov](https://img.shields.io/codecov/c/github/jevandezande/pipenv-cookiecutter)](https://app.codecov.io/gh/jevandezande/pipenv-cookiecutter/)

[Cookiecutter](https://github.com/audreyr/cookiecutter) for setting up pipenv projects with all of the below features.

## Features
- Testing with [pytest](https://docs.pytest.org/en/latest/)
- Formatting with [black](https://github.com/psf/black)
- Import sorting with [isort](https://github.com/timothycrosley/isort)
- Static typing with [mypy](http://mypy-lang.org/)
- Linting with [flake8](http://flake8.pycqa.org/en/latest/)
- Git hooks that run all the above with [pre-commit](https://pre-commit.com/)
- Continuous Integration with [GitHub Actions](https://github.com/features/actions)
- Code coverage with [Codecov](https://codecov.io)


## Setup
While all of the steps are automated, you will need to install `pipenv`.
Additionally, `pipx` is recommended for installing any command line tools.

```sh
python3 -m pip install pipx
pipx ensurepath

# Install pipenv using pipx
pipx install pipenv

# Use cookiecutter to create project from this template
pipx run cookiecutter gh:jevandezande/pipenv-cookiecutter
```


The cookiecutter will automagically
- Generate a repo with the input configuration
- Initialise git
- Install dependencies
- Setup pre-commit and pre-push hooks
- Make initial commit


## Recommendations
Make a `cookiecutter.yml` configuration file (see `template_config.yml`) with
your default settings and use it with the flag `--config-file cookiecutter.yml`
