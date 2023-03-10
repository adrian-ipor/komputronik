import os


def mkdir_recursive(path: str):
    sub_path = os.path.dirname(path)
    if not os.path.exists(sub_path) and sub_path != '':
        mkdir_recursive(sub_path)
    if not os.path.exists(path):
        os.mkdir(path)