import operation
import ui

def run():
    command = ''
    while command != '7':
        ui.menu()
        command = input().strip()
        if command == '1':
            operation.show('all')
        elif command == '2':
            operation.add()
        elif command == '3':
            operation.show('id')
            operation.id_delete()
        elif command == '4':
            operation.show('id')
            operation.id_rewrite()
        elif command == '5':
            operation.show('date')
            operation.date_show()
        elif command == '6':
            operation.show('id')
            operation.id_show()
        elif command == '7':
            bye()
            break
        else:
            print('Такой команды нет. Проверьте правильность ввода!')


def bye():
    print('До скорых встреч!')