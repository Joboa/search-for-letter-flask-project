def view_tasks():
    all_task = []
    with open('todos.txt') as tasks:
        for task in tasks:
            all_task.append([])
            for item in task.split('|'):
                all_task[-1].append(item)
    print(str(all_task))


view_tasks()