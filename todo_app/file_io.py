# todo_app/file_io.py

import json
import os

def save_tasks_to_file(task_manager, filepath="tasks.json"):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(task_manager.to_dict_list(), f, ensure_ascii=False, indent=4)

def load_tasks_from_file(task_manager, filepath="tasks.json"):
    if not os.path.exists(filepath):
        return
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
        task_manager.from_dict_list(data)
