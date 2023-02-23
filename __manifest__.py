{
    'name': 'Employee Level',
    'version': '16.0.1.0.0',
    'sequence': 1,
    'summary': 'Employee Level',
    'category': 'Sales',
    'installable': True,
    'auto_install': False,
    'depends': ['hr','base'],
    'data': [
    'security/ir.model.access.csv',
    'data/employee_level_data.xml',
    'views/employee_level_view.xml',
    'views/employee_inherit.xml',
    'views/employee_level_menu.xml'
    ]}