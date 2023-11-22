
from unittest.mock import Mock
from lib.task_list import TaskList

class TestTaskList:
    def setUp(self):
        self.task_list = TaskList()

    def test_add_mock_task(self):
        mock_task = Mock()
        self.task_list.add(mock_task)
        self.assertIn(mock_task, self.task_list.tasks)

    def test_all_complete_with_mocks(self):
        mock_task1 = Mock()
        mock_task2 = Mock()

        mock_task1.is_complete.return_value = True
        mock_task2.is_complete.return_value = True

        self.task_list.add(mock_task1)
        self.task_list.add(mock_task2)

        self.assertTrue(self.task_list.all_complete())

    def test_not_all_complete_with_mocks(self):
        mock_task1 = Mock()
        mock_task2 = Mock()

        mock_task1.is_complete.return_value = True
        mock_task2.is_complete.return_value = False

        self.task_list.add(mock_task1)
        self.task_list.add(mock_task2)

        self.assertFalse(self.task_list.all_complete())

    def test_all_method(self):
        mock_task1 = Mock()
        mock_task2 = Mock()

        self.task_list.add(mock_task1)
        self.task_list.add(mock_task2)

        self.assertEqual(self.task_list.all(), [mock_task1, mock_task2])

