{
    'name': 'Invoice Payments Widget',
    'version': '1.0',
    'description': 'Invoice payments widget',
    'summary': '',
    'author': 'Centricital',
    'website': '',
    'license': 'LGPL-3',
    'category': '',
    'depends': [
        'account',
        'base_automation'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/account_move.xml'
    ],
    'auto_install': False,
    'application': False,
}
