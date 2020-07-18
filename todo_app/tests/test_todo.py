from odoo.tests.common import TransactionCase


class TestTodo(TransactionCase):
    def test_create(self):
        # "Create a simple Todo"
        todo = self.env['todo.task']
        task = todo.create({'name': 'test task'})
        self.assertEqual(task.is_done, False)
