import os
import pickle
import time

my_file = "database.txt"
my_directory = 'files'
file_name = 'book'


def check_exist(dir):
    if os.path.exists(dir):
        return dir
    else:
        os.mkdir(dir)
        return dir


def save_obj(name):
    with open(my_directory + os.sep + file_name + '.pkl', 'wb') as f:
        pickle.dump(name, f, pickle.HIGHEST_PROTOCOL)


def load_obj(name):
    with open(my_directory + os.sep + name + '.pkl', 'rb') as f:
        return pickle.load(f)


def add_to_dict():
    name = input('Enter name: ')
    adress = input('Enter adress: ')
    if name not in book:
        book[name] = adress
    else:
        print('this name is also in adresbook')


def del_from_dict():
    name = input('Enter name: ')
    if name in book:
        del book[name]
        return 1
    else:
        return None


def find_in_dict():
    name = input('Enter name: ')
    if name in book:
        return book[name]
    else:
        return None


def print_all_dict():
    for name, adress in book.items():
        print(f"{name}: {adress}")


if __name__ == "__main__":
    check_exist(my_directory)
    book = load_obj(file_name)
    x = '1'
    while (x != '0'):
        x = input("1 - add  2 - find  3 - see all  4 - delete  0 - exit\n")
        print('wait...')
        time.sleep(0.6)

        if x == '1':
            add_to_dict()
        elif x == '2':
            y = find_in_dict()
            if y != None:
                print(y)
            else:
                print('nothing')
        elif x == '3':
            print_all_dict()
        elif x == '4':
            del_from_dict()
        elif x == '0':
            save_obj(book)
            print('close')
            time.sleep(0.2)
