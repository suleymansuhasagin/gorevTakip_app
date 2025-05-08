# tests/test_task_manager.py

import unittest
from todo_app.task_manager import TaskManager

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        self.manager.add_task("Test görev")
        self.assertEqual(len(self.manager.tasks), 1)
        self.assertEqual(self.manager.tasks[0].title, "Test görev")

    def test_complete_task(self):
        self.manager.add_task("Görev tamamla")
        self.manager.complete_task(0)
        self.assertTrue(self.manager.tasks[0].completed)

    def test_remove_task(self):
        self.manager.add_task("Görev sil")
        self.manager.remove_task(0)
        self.assertEqual(len(self.manager.tasks), 0)

if __name__ == '__main__':
    unittest.main()
