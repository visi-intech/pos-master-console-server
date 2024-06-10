{
    'name': 'VIT Demo POS',
    'version': '17.0.1.0.0',
    'category': 'Point of Sale',
    'summary': """Belong to VIT""",
    'author': 'Visi Intech',
    'company': 'Visi Intech',
    'maintainer': 'Visi Intech',
    'website': "https://www.Visi-Intech.com",
    'depends': ['point_of_sale'],
    'data': [
        'security/ir.model.access.csv',
        # 'views/views_card_number.xml',
        'views/views_pos_order.xml',
        'views/views_cashback_sellout.xml',
        'views/views_stock_picking.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}