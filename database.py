def add_data(data_str):
    with open('file.txt', 'a', encoding='UTF-8') as f:
        f.write(data_str)


def find_person(data_str):
     with open('file.txt', 'r', encoding='UTF-8') as f:
        lst_str = f.readlines()
        for worker in lst_str:
            if data_str in worker:
                print(worker)
                return worker

def change_name(data_str, new_name):
    with open('file.txt', 'r+', encoding='UTF-8') as f:
         lines = f.readlines()
         f.seek(0)
         for line in lines:
            if line != data_str:
                f.write(line)
            else:
                f.write(line.replace(data_str, new_name))
         f.truncate()

def delete_user(full_name):
    with open('file.txt', 'r+', encoding='UTF-8') as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            if line != full_name:
                f.write(line)
        f.truncate()