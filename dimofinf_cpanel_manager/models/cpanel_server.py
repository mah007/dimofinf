
from odoo import models, fields

class CPanelServer(models.Model):
    _name = 'cpanel.server'

    datacenter_id = fields.Many2one('cpanel.datacenter', string="Data Center")
    packages = fields.One2many('cpanel.package', 'server_id', string="Available Packages")

    api_url = fields.Char(string="API URL")
    api_token = fields.Char(string="API Token")
