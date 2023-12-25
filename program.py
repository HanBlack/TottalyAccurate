import os


def current_directory():
    current_directory_variable = os.path.dirname(os.path.realpath(__file__))
    return current_directory_variable
