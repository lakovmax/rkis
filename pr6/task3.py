class Task:
    def __init__(self, date_start, date_finish, description):
        self.DateStart = date_start
        self.DateFinish = date_finish
        self.Description = description

    def __str__(self):
        return f"Описание: {self.Description}, Начало: {self.DateStart}, Окончание: {self.DateFinish}"

tasks = [
    Task("2025-06-01", "2025-07-01", "Task1"),
    Task("2025-12-01", "2026-05-24", "Task2"),
    Task("2025-06-01", "2025-06-02", "Task3"),
    Task("2025-01-10", "2025-02-01", "Task4"),
    Task("2023-07-03", "2023-07-29", "Task5"),
]

latest_task = tasks[0]
for task in tasks[1:]:
    if task.DateFinish > latest_task.DateFinish:
        latest_task = task

print(f"Занятие, заканчивающееся позже всех:\n{latest_task}")