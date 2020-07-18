from odoo import fields, models


class TodoStage(models.Model):
    _name = 'todo.task.stage'
    _description = 'To-do Stage'
    _order = 'sequence,name'

    # string fields
    name = fields.Char("Name")
    desc = fields.Text("Description")
    state = fields.Selection(
        [('draft', 'new'),
         ('Open', 'Started'),
         ('done', 'closed')], 'State')
    docs = fields.Html('Documentation')

    # numeric Field
    sequence = fields.Integer('Sequence')
    perc_complete = fields.Float('% Complete', (3, 2))

    # date field

    date_effective = fields.Date("Effecvtive Date")
    date_created = fields.Datetime(
        'Create Date and Time',
        default=lambda self: fields.Datetime.new()
    )

    # other
    fold = fields.Boolean('Folded')
    image = fields.Binary('Image')
