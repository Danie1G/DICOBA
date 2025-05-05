{
    'name': 'Sead Invoice Payments Widget',
    'version': '1.0',
    'description': 'Invoice payments widget',
    'summary': '',
    'author': 'Jhon Jairo Rojas Ortiz',
    'website': '',
    'license': 'LGPL-3',
    'category': '',
    'depends': [
        'account',
        'base_automation'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/invoice_widget.xml',
        'views/account_move.xml'
    ],
    'auto_install': False,
    'application': False,
}
