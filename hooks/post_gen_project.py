from __future__ import annotations

import logging
import os
import shutil
import sys
from datetime import datetime
from subprocess import check_call
from typing import Optional

logger = logging.Logger("post_gen_project_logger")
logger.setLevel(logging.INFO)


def call(*inputs):
    """
    Call shell commands.
    Warning: strings with spaces are not yet supported.
    """
    for input in inputs:
        logger.debug(input)
        check_call(input.split())


def set_python_version():
    python_version = f"{sys.version_info.major}.{sys.version_info.minor}"
    if sys.version_info.minor < 9:
        logger.warn(f"{python_version=} should be upgraded to the latest avaiable python version.")

    file_names = [
        ".github/workflows/test.yml",
        "Pipfile",
        "setup.cfg",
    ]

    for file_name in file_names:
        with open(file_name) as f:
            contents = f.read().replace("{python_version}", python_version)
        with open(file_name, "w") as f:
            f.write(contents)


def set_license(license: Optional[str] = "MIT"):
    if not license:
        return

    license = license.lower()

    # license_dir = os.path.dirname(os.path.abspath(__file__)) + "../licenses"
    license_dir = os.path.expanduser("~/.cookiecutters/pipenv-cookiecutter/licenses/")

    licenses = list(map(os.path.basename, os.listdir(license_dir)))  # type:ignore
    if license not in licenses:
        raise ValueError(f"{license=} is not available yet. Please select from:\n{licenses=}")

    shutil.copy(f"{license_dir}/{license}", "LICENSE")

    with open("LICENSE") as f:
        contents = f.read().replace("{year}", f"{datetime.now().year}")
        contents = contents.replace("{author_name}", "{{cookiecutter.author_name}}")
    with open("LICENSE", "w") as f:
        f.write(contents)


def git_init():
    call("git init")


def update_pipfile():
    with open("Pipfile") as f:
        # Extra space and .strip() prevents issues with quotes
        contents = (
            f.read()
            .replace("{pip_packages}", """{{cookiecutter.pip_packages}} """.strip())
            .replace(
                "{pip_dev_packages}",
                """{{cookiecutter.pip_dev_packages}} """.strip(),
            )
        )
    with open("Pipfile", "w") as f:
        f.write(contents)

    call("pipenv update")


def install_dev():
    call("pipenv install --dev")


def git_hooks():
    call("pipenv run pre-commit install -t pre-commit", "pipenv run pre-commit install -t pre-push")


def git_initial_commit():
    call("git add .", "git commit -m Setup")


def git_add_remote(name, location):
    call(f"git remote add {name} {location}")


SUCCESS = "\x1b[1;32m"
TERMINATOR = "\x1b[0m"


def main():
    set_python_version()
    set_license("{{cookiecutter.license}}")
    git_init()
    update_pipfile()
    install_dev()
    git_hooks()
    git_initial_commit()
    git_add_remote("origin", "{{cookiecutter.project_url}}")

    print(f"{SUCCESS}Project successfully initialized{TERMINATOR}")


if __name__ == "__main__":
    main()
