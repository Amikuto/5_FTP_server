import os
import pickle
import shutil
import logging
# from settings import PATH

# PATH = os.path.join(os.getcwd(), 'docs')
# os.chdir("/docs")
logging.basicConfig(filename="ftp-server.log", level=logging.INFO)
PATH = os.getcwd()


def copy_file(name):
    return pickle.dumps(name)


def files_in_curr_directory():
    file_list = '; '.join(os.listdir())
    if file_list == "":
        return "Папка пуста"
    else:
        return file_list


def current_dir():
    return os.getcwd().replace("D:\Programming\Python\\5_FTP_server\docs", "/")


def create_folder(name):
    """
    1 задание - создает папку в текущей директории
    :param name:
    :return:
    """
    try:
        os.mkdir(name)
        return f"Папка {name} создана!"
    except OSError:
        logging.warning("Ошибка в создании папки!")
        return "Папку создать не удалось!"


def delete_folder(name):
    """
    2 задание - удаляет папку в текущей директории
    :param name:
    :return:
    """
    print(name)
    try:
        os.rmdir(name)
        return f"Папка {name} удалена!"
    except OSError:
        logging.warning("Ошибка в удалении папки!")
        return "Удалить папку не удалось!"


def change_dir(path):
    """
    3 задание - изменяет текущую директорию
    :param path:
    :return:
    """
    global curr_path

    if os.getcwd().split("\\")[-1] == "2-Task" and path == "..":
        return "Ошибка! Выход за пределы директории"
    else:
        try:
            if path == "..":
                x = os.getcwd().split("\\")
                os.chdir(path)
                curr_path = curr_path.replace("\\" + x[-1], "")
                return "Текущая директория -", curr_path
            else:
                os.chdir(path)
                x = os.getcwd().split("\\")
                curr_path = curr_path + "\\" + x[-1]

                return "Текущая директория - ", curr_path
        except FileNotFoundError:
            logging.warning("Ошибка в изменении текущей директории!")
            return "Ошибка! Либо папка указана неверно, либо такой папки не существует"


def create_file(name):
    """
    4 задание - создает новый файл
    :param name:
    :return:
    """
    try:
        open(name, "w", encoding="UTF-8").close()
        return f"Файл {name} создан!"
    except Exception:
        logging.warning("Ошибка в создании нового файла!")
    # my_file.close()


def add_text_to_file(file_name, text):
    """
    5 задание - добавляет текст в конец файла
    :param file_name:
    :param text:
    :return:
    """
    try:
        with open(file_name, "a") as f:
            data = text + "\n"
            f.write(data)
    except IOError:
        logging.warning(f"Ошибка в добавлении текста в файл {file_name}!")
        return "Возникла ошибка IOError!"


def show_text(file_name):
    """
    6 задание - показывает содержимое файла
    :param file_name:
    :return:
    """
    try:
        with open(f"{PATH}\{file_name}", "r") as f:
            text = f.read()
            return text
    except IOError:
        logging.warning(f"Ошибка в выводе содержимого файла {file_name}!")
        return "Возникла ошибка IOError!"


def remove_file(file_name):
    """
    7 задание - удаляет файл в текущей директории
    :param file_name:
    :return:
    """
    try:
        os.remove(file_name)
        return f"Папка {file_name} удалена!"
    except OSError:
        logging.warning(f"Ошибка в удалении файла {file_name}!")
        return f"Удалить папку с названием {file_name} не удалось!"


def copy_file(file_name, new_file_name):
    """
    8 задание - копирует файлы
    :param file_name: название текущего файла
    :param new_file_name: название нового файла
    :return:
    """
    path = curr_path + "\\" + new_file_name
    shutil.copyfile(file_name, path)


def move_file(file_name, path):
    """
    9 задание - Перемещает файл в новую директорию
    :param file_name:
    :param path:
    :return:
    """
    new_dir = os.path.join(curr_path, path)
    check_path(new_dir)
    shutil.move(file_name, path)
    logging.warning("Файл перемещен!")


def rename_file(file_name, new_file_name):
    """
    10 задание - Изменяет название файла
    :param file_name:
    :param new_file_name:
    :return:
    """
    try:
        os.rename(file_name, new_file_name)
        return f"Файл {file_name} изменен на {new_file_name}"
    except Exception:
        return f"Удалить файл не удалось!"


def check_path(path) -> bool:
    if path not in PATH:
        return True
    else:
        return False
