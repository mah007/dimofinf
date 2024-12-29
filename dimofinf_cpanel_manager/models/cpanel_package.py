
from odoo import models, fields

class CPanelPackage(models.Model):
    _name = 'cpanel.package'
    _description = 'cPanel Package'

    name = fields.Char(string="Package Name", required=True)
    description = fields.Text(string="Description")
    disk_space = fields.Float(string="Disk Space (GB)")
    max_databases = fields.Integer(string="Max Databases")
    max_email_accounts = fields.Integer(string="Max Email Accounts")
    price = fields.Float(string="Price")
