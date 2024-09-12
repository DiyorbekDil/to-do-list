from crud import show_tasks, add_task, change_task_status, delete_task
from crud import change_task_position


def to_do():
    text = """
    1. Vazifa qo'shish
    2. Vazifalarni ko'rish
    3. Vazifani o'chirish
    4. Vazifa statusini o'zgartirish
    5. Vazifa o'rnini almashtirish
    6. Chiqish
    """
    print(text)

    user_input = input('Enter a number: ')
    if user_input == '1':
        add_task()
        to_do()
    elif user_input == '2':
        show_tasks()
        to_do()
    elif user_input == '3':
        delete_task()
        to_do()
    elif user_input == '4':
        change_task_status()
        to_do()
    elif user_input == '5':
        change_task_position()
        to_do()
    elif user_input == '6':
        return
    else:
        print('Unexpected character, try again')
        return to_do()


if __name__ == '__main__':
    to_do()
