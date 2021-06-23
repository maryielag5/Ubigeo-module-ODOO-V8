# -*- coding: utf-8 -*-
{
    'name': 'Ubigeo - UNDAC',
    'version': '2.0',
    'category': 'Generic Modules',
    'description': """
                    Modulo Ubigeo para la Undac.
                    """,
    'author': 'Undac',
    'website': 'https://www.undac.edu.pe',
    'depends': [
        'web',
        'base',
        'hr',
    ],
    'data': [
        'xml/res_country_data.xml',
        # 'security/ir.model.access.csv',
    ],
    'update_xml': [],
    'installable': True,
    'auto_install': False,
}
