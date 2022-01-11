from re import match

MODULE_REGEX = r"^[a-zA-Z][_a-zA-Z0-9]+$"
module_name = "{{cookiecutter.repo_name}}"

if not match(MODULE_REGEX, module_name):
    raise ValueError(f"{module_name=} is not a valid Python module name.")
