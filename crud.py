from database import execute_query
from models import tasks


def add_task():
    all_tasks = get_tasks()
    if all_tasks:
        priority = all_tasks[-1][3] + 1
    else:
        priority = 1
    title = input('Task title: ')
    query = tasks.insert().values(title=title, priority=priority)
    execute_query(query=query)
    print('Added')


def get_tasks():
    query = tasks.select().order_by(tasks.c.priority)
    result = execute_query(query=query)
    return result.fetchall()


def show_tasks():
    all_tasks = get_tasks()
    print("Title - Status - Priority")
    for task in all_tasks:
        print(f"{task[1]} - {task[2]} - {task[3]}")


def is_available_this_task(task_priority):
    all_tasks = get_tasks()
    for task in all_tasks:
        if task[3] == task_priority:
            return True
    else:
        return False


def change_task_status():
    try:
        task_priority = int(input('Enter task priority: '))
        if not is_available_this_task(task_priority):
            print('There is no such task priority')
        else:
            query = tasks.update().where(tasks.c.priority == task_priority).values(status=True)
            execute_query(query)
            print('Status changed!')
    except ValueError:
        print("Task priority must be a whole number")


def delete_task():
    try:
        task_priority = int(input('Enter task priority: '))
        if not is_available_this_task(task_priority):
            print('There is no such task priority')
        else:
            query = tasks.delete().where(tasks.c.priority == task_priority)
            execute_query(query)
            query = tasks.update().where(tasks.c.priority > task_priority).values(priority=tasks.c.priority-1)
            execute_query(query)
            print('Deleted!')
    except ValueError:
        print("Task priority must be a whole number")


def get_task_id(priority):
    query = tasks.select().where(tasks.c.priority == priority)
    result = execute_query(query)
    return result.fetchone()[0]


def change_task_position():
    try:
        task_priority = int(input('O\'zgartirmoqchi bo\'lgan taskingiz prioritysini kiriting: '))
        new_priority = int(input('Qaysi priorityga ko\'tarmoqchisiz yoki tushirmoqchisiz: '))
        if not (is_available_this_task(task_priority) and is_available_this_task(new_priority)):
            print('Bunday prioritylar bo\'lmasligi mumkin, qayta urining!')
        else:
            task_id = get_task_id(task_priority)
            if task_priority > new_priority:
                query = tasks.update().values(priority=tasks.c.priority+1)\
                    .where(new_priority <= tasks.c.priority).where(tasks.c.priority < task_priority)
                execute_query(query)
            else:
                query = tasks.update().values(priority=tasks.c.priority-1)\
                    .where(task_priority < tasks.c.priority).where(tasks.c.priority <= new_priority)
                execute_query(query)
            query = tasks.update().values(priority=new_priority).where(tasks.c.id == task_id)
            execute_query(query)
            print('Changed!')
    except ValueError:
        print("Task priority must be a whole number")
