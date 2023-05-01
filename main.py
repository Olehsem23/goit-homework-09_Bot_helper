# Бот-помічник. Розпізнає команди, що вводяться з клавіатури, і відповідає відповідно до введеної команди.


USERS = {}  # Створюємо словник з іменами та телефонами


def input_error(func):  # decorator
    def inner(*args):
        try:
            result = func(*args)
            return result
        except KeyError:
            return "No user"
        except ValueError:
            return 'Give me name and phone please'
        except IndexError:
            return 'Enter user name'
    return inner


def hello_user(_):  # Відповідь на команду 'Hello'
    return "Hello! How can I help you?"


def unknown_command(_):  # Якщо команди нема у словнику HANDLERS, то виводимо: 'unknown command'
    return "Unknown command"


def exit_program(_):  # Вихід з програми відбувається при введенні команд: goodbye, close, exit
    return


@input_error
def add_user(args):  # Додаємо нового користувача і телефон до словника USERS.
    name, phone = args
    USERS[name] = phone
    return f'User {name} added!'


@input_error
def change_phone(args):  # Заміна телефона для користувача.
    name, phone = args
    old_phone = USERS[name]
    USERS[name] = phone
    return f'{name} has new number: {phone} Old number: {old_phone}'


@input_error
def show_phone(args):  # Пошук телефона вибраного користувача.
    name = args[0]
    phone = USERS[name]
    return f'{name} has phone: {phone}'


def show_all(_):  # Видрукувати весь список імен і телефонів зі словника USERS. Якщо словник порожній, то exit
    result = ''
    for name, phone in USERS.items():
        result += f'Name: {name} phone: {phone}\n'
    return result


# Словник усіх команд, які приймає бот, якщо ж таких команд нема, то видасть: 'unknown command'
HANDLERS = {
    'hello': hello_user,
    'add': add_user,
    'change': change_phone,
    'phone': show_phone,
    'show all': show_all,
    'exit': exit_program,
    'good bye': exit_program,
    'goodbye': exit_program,
    'close': exit_program,
}


def parse_input(user_input):  # Парсер команд
    command, *args = user_input.split()
    command = command.lstrip()

    try:
        handler = HANDLERS[command.lower()]
    except KeyError:
        if args:
            command = command + ' ' + args[0]
            args = args[1:]
        handler = HANDLERS.get(command.lower(), unknown_command)
    return handler, args


def main():  # Ввід даних
    while True:
        # example: add Petro 0991234567
        user_input = input('Please enter command and args: ')
        handler, *args = parse_input(user_input)
        result = handler(*args)
        if not result:
            print('Exit')
            break
        print(result)


if __name__ == "__main__":  # Точка входження
    main()
