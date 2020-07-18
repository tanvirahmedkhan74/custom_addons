from odoo import fields, models


class TodoTag(models.Model):
    _name = 'todo.task.tag'
    _description = 'To-do Tag'

    name = fields.Char('Name', _translate=True)
