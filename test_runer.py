import sys
import importlib

if __name__ == "__main__":
    file_name = sys.argv[1]
    importlib.import_module(file_name)
    mod = sys.modules[file_name]
    for name in dir(mod):
        fun_candidate = getattr(mod, name)
        if callable(fun_candidate) and name.endswith("_test"):
            fun_candidate()
            print("Running: ", name, "\n")