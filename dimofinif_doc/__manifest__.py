{
    'name': 'Dimofinf Document Layout',
    'version': '1.0',
    'author': 'Mahmoud Abdel Latif',
    'category': 'Customization',
    'summary': 'Custom header and footer for documents',
    'description': """
        Adds custom header and footer for documents in Odoo 17.
    """,
    'depends': ['base', 'web', 'account'],
    'data': [
        'views/dimofinf_doc_layout.xml',
        # 'views/report_invoice_custom.xml',
    ],
    'assets': {
        'web.report_assets_common': [
            'dimofinif_doc/static/src/css/dds.css',
        ],
    },
    'installable': True,
    'application': True,
'license': 'LGPL-3',
}