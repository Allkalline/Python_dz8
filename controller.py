import view
import database

def main():
    while True:
        op = view.get_op()
        if op == 1:
            data_worker = view.get_data()
            database.add_data(data_worker)
        if op == 2:
            find_str = view.find_person()
            find_str = database.find_person(find_str)
            #print(find_str)
            op2 = view.ask2()
            if op2 == 1:
                new_name = view.get_data()
                database.change_name(find_str,new_name)
                print('Запись изменена')
            if op2 == 2:
                database.delete_user(find_str)
                print('Запись удалена')
        if op == 3:
            break

if __name__=="__main__":
    main()