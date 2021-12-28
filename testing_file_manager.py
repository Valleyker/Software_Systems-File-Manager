import os
import sys
import shutil
import pytest

not_path_dir = "/Users/user/MP/workdir/TESTING"
path_dir = "/Users/user/MP/workdir/TESTING"
path_file = "/Users/user/MP/workdir/test"
not_path_file = "/Users/user/MP/workdir/test"


@pytest.fixture
def makeDir():  # Создает папку
    if "workdir" not in path_dir:
        print("Ошибка, вы вне папки workdir")
    else:
        os.mkdir(path_dir)
        return True


@pytest.fixture
def removeDir():  # Удаление папки
    if "workdir" not in path_dir:
        print("Ошибка, вы вне папки workdir")
    else:
        os.rmdir(path_dir)
        return True


@pytest.fixture
def create_file():  # создать файл
    file = open(path_file, 'a+')
    file.close()
    return True


# Запись в файл
@pytest.fixture
def writefile():
    try:
        phrase = "Hello "
        file = open(path_file, 'a+')
        file.write(phrase)
        file.close()
        print("В файл записано 'Hello'")
        return True
    except FileNotFoundError:
        print("File not found")


@pytest.fixture
def readFile():  # просмотреть содержимое текстового файла
    try:
        with open(path_file) as file:
            for line in file:
                print(line)
        return True
    except FileNotFoundError:
        print("File not found")


@pytest.fixture
def remFile():  # удалить файл
    try:
        file = "/Users/user/MP/workdir/test_for_rm"
        os.remove(file)
        print("Файл удален")
        return True
    except FileNotFoundError:
        print("File not found")


@pytest.fixture
def movFile():  # переместить файл
    try:
        file = "/Users/user/MP/workdir/test_renamed"
        file2 = "/Users/user/MP/workdir/new_test_renamed"
        shutil.copyfile(file, file2)
        os.remove(file)
        print("Файл перемещен")
        return True
    except FileNotFoundError:
        print("File not found")


@pytest.fixture
def copyFile():  # копировать файл
    try:
        coping = "/Users/user/MP/workdir/test2"
        shutil.copyfile(path_file, coping)
        print("Файл скопирован")
        return True
    except FileNotFoundError:
        print("File not found")


@pytest.fixture
def renameFile():  # переим-ть файл
    try:
        print("введите новое название ")
        renamed = "/Users/user/MP/workdir/test_renamed"
        os.rename(path_file, renamed)
        print("Файл перименован")
        return True
    except FileNotFoundError:
        print("File not found")


'''
НЕГАТИВНЫЕ ТЕСТЫ
'''


@pytest.fixture
def negative_makeDir():  # Создает папку в несуществующей директории
    if "workdir" not in not_path_dir:
        print("Ошибка, вы вне папки workdir")
    else:
        os.mkdir(path_dir)
        return True


@pytest.fixture
def negative_removeDir():  # Удаление папки в несущетсвующей директории
    if "workdir" not in not_path_dir:
        print("Ошибка, вы вне папки workdir")
    else:
        os.rmdir(path_dir)
        return True


@pytest.fixture
def negative_create_file():  # создать файл
    file = open(not_path_file, 'a+')
    file.close()
    return True


@pytest.fixture()
def negative_movFile():  # Негативный тест по перемещению несуществующего файла .
    try:
        file = "/Users/user/MP/workdir/not_test"
        file2 = "/Users/user/MP/workdir/new_test_renamed"
        shutil.copyfile(file, file2)
        os.remove(file)
        print("Файл перемещен")
        return True
    except FileNotFoundError:

        print("File not found")


# негативный тест - Запись в несуществующий файл
@pytest.fixture
def negative_writefile():
    try:
        phrase = "Hello"
        file = open(not_path_file, 'a+')
        file.write(phrase)
        file.close()
        print("В файл записано 'Hello'")
        return True
    except FileNotFoundError:
        print("File not found")


@pytest.fixture()
def negative_remFile():  # Негативный тест на удаление несуществующего файла
    try:
        file = "/Users/user/MP/workdir/not_test_for_rm"
        os.remove(file)
        print("Файл удален")
        return True
    except FileNotFoundError:
        print("File not found")


@pytest.fixture
def negative_readFile():  # негативный тест - просмотреть содержимое несуществующего текстового файла
    try:
        with open(not_path_file) as file:
            for line in file:
                print(line)
        return True
    except FileNotFoundError:
        print("File not found")


@pytest.fixture
def negative_copyFile():  # негативный тест - копировать несуществующий файл
    try:
        coping = "/Users/user/MP/workdir/test2"
        shutil.copyfile(not_path_file, coping)
        print("Файл скопирован")
        return True
    except FileNotFoundError:
        print("File not found")


@pytest.fixture
def negative_renameFile():  # переим-ть несуществующий файл
    try:
        renamed = "/Users/user/MP/workdir/test_renamed"
        os.rename(not_path_file, renamed)
        print("Файл перименован")
        return True
    except FileNotFoundError:
        print("File not found")


def test_dir_work_1(makeDir):
    assert (makeDir == 1)


def test_rm_dir(removeDir):
    assert (removeDir == 1)


def test_create_file(create_file):
    assert (create_file == 1)


def test_writefile(writefile):
    assert (writefile == 1)


def test_read_file(readFile):
    assert (readFile == 1)


def test_cp_file(copyFile):
    assert (copyFile == 1)


def test_rn_file(renameFile):
    assert (renameFile == 1)


def test_mv_file(movFile):
    assert (movFile == 1)



def test_rm_file(remFile):
    assert (remFile == 1)

@pytest.mark.xfail()
def test_negative_makeDir(negative_makeDir):
    assert (negative_makeDir == 1)


@pytest.mark.xfail()
def negative_test_rm_dir(negative_removeDir):
    assert (negative_removeDir == 1)


@pytest.mark.xfail()
def negative_test_create_file(negative_create_file):
    assert (negative_create_file == 1)


@pytest.mark.xfail()
def negative_test_writefile(negative_writefile):
    assert (negative_writefile == 1)


@pytest.mark.xfail()
def negative_test_read_file(negative_readFile):
    assert (negative_readFile == 1)


@pytest.mark.xfail()
def negative_test_cp_file(negative_copyFile):
    assert (negative_copyFile == 1)


@pytest.mark.xfail()
def negative_test_rn_file(negative_renameFile):
    assert (negative_renameFile == 1)


@pytest.mark.xfail()
def negative_test_mv_file(negative_movFile):
    assert (negative_movFile == 1)


@pytest.mark.xfail()
def negative_test_rm_file(negative_remFile):
    assert (negative_remFile == 1)
