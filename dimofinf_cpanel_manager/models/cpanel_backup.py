import requests
from odoo import models, fields, api, exceptions

class CPanelBackup(models.Model):
    _name = 'cpanel.backup'
    _description = 'cPanel Backup Management'

    name = fields.Char(string="Backup Name", required=True)
    date = fields.Datetime(string="Backup Date")
    size = fields.Integer(string="Backup Size (MB)")
    server_id = fields.Many2one('cpanel.server', string="Server", required=True)

    def create_backup(self):
        url = f"{self.server_id.api_url}/create_backup"
        headers = {'Authorization': f"Bearer {self.server_id.api_token}"}
        response = requests.post(url, headers=headers)
        if response.status_code != 200:
            raise exceptions.UserError(f"Failed to create backup: {response.text}")
