
from odoo import models, fields

class CPanelAccount(models.Model):
    _name = 'cpanel.account'

    customer_id = fields.Many2one('res.partner', string="Customer", required=True)
