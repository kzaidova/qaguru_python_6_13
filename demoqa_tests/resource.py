from pathlib import Path

def path(file_name):
    return str(
        Path(qaguru_python_6_13.__file__).parent.joinpath(f'resources/{file_name}').absolute()
    )