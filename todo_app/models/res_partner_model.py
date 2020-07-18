from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'
    todo_ids = fields.Many2many(comodel_name='todo.task', string='To-do Teams')
