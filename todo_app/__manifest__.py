{
    'name': 'To-Do Application',
    'description': 'Manage personal to-do tasks.',
    'author': 'Tanvir Ahmed',
    'depends': ['base'],
    'application': True,
    'data': ['views/todo_menu.xml',
             'views/todo_view.xml',
             'views/res_partner_view.xml',
             'security/ir.model.access.csv',
             'security/todo_access_rules.xml',
             'views/index_template.xml',
             ],

}
