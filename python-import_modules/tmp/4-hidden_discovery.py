#!/usr/bin/python3
import marshal
import types

def discover_names(pyc_file):
    with open(pyc_file, 'rb') as f:
        f.read(16)  # skip header
        code = marshal.load(f)

    # create module object to execute code
    module = types.ModuleType("hidden_4")
    exec(code, module.__dict__)

    # get names defined in module
    names = dir(module)

    # filter out names starting with '__'
    filtered_names = [name for name in names if not name.startswith('__')]

    # alphabetically
    sorted_names = sorted(filtered_names)

    return sorted_names

if __name__ == "__main__":
    pyc_path = "hidden_4.pyc"
    names = discover_names(pyc_path)

    for name in names:
        print(name)
