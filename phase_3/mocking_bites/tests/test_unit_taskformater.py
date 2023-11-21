import unittest
from unittest.mock import Mock
from lib.taskformatter import TaskFormatter
from lib.task import Task  # Assuming this is the real Task class

class TestTaskFormatter(unittest.TestCase):
    def test_format_incomplete_task(self):
        # Create a mock task
        mock_task = Mock(spec=Task)
        mock_task.title = "Incomplete Task"
        mock_task.is_complete.return_value = False

        formatter = TaskFormatter(mock_task)
        expected_format = "- [ ] Incomplete Task"
        self.assertEqual(formatter.format(), expected_format)

    def test_format_complete_task(self):
        # Create a mock task
        mock_task = Mock(spec=Task)
        mock_task.title = "Complete Task"
        mock_task.is_complete.return_value = True

        formatter = TaskFormatter(mock_task)
        expected_format = "- [x] Complete Task"
        self.assertEqual(formatter.format(), expected_format)

if __name__ == '__main__':
    unittest.main()