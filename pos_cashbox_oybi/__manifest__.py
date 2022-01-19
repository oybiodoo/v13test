# -*- coding: utf-8 -*-
{
    'name': "PoS Open Cashbox",

    'summary': """
        Open Cashbox on closed PoS sessions""",

    'description': """
        Own Your BI: Open Cashbox on Closed PoS Sessions.
        Dev Task ID: 2380001
    """,
    'author': "Odoo Inc",
    'website': "http://www.odoo.com",
    'category': 'Custom Development',
    'version': '0.1',
    'license': 'OEEL-1',
    'depends': ['pos_epson_printer'],
    'data': [
        'views/pos_config_views.xml',
        'views/point_of_sale_assets.xml',
    ],
}
