import os
import tkinter.messagebox as msg


def generic_msg(title='Alert', text='Not ready yet.\nSorry'):
    """
    Shows the user a msg

    :param title: str
    :param text: str
    :return: None
    """
    msg.showinfo(title, text)


def parse_filename(path):
    """
    Splits the path by the os.sep and returns the last name in the
    path

    :param path: str
    :return: str
    """
    return path.split(os.sep)[-1]