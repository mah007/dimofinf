
from odoo import models, fields, api, exceptions

class CPanelDatabase(models.Model):
    _name = 'cpanel.database'
    _description = 'cPanel Database Management'

    name = fields.Char(string="Database Name", required=True)
    user = fields.Char(string="Database User", required=True)
    password = fields.Char(string="Password", required=True)
    domain = fields.Many2one('cpanel.account', string="Domain", required=True)

    def create_database(self):
        url = f"{self.domain.server_id.api_url}/create_database"
        headers = {'Authorization': f"Bearer {self.domain.server_id.api_token}"}
        payload = {
            'database': self.name,
            'user': self.user,
            'password': self.password,
            'domain': self.domain.name
        }
        try:
            response = requests.post(url, headers=headers, json=payload)
            if response.status_code != 200:
                raise exceptions.UserError("Failed to create database.")
        except requests.RequestException as e:
            raise exceptions.UserError(f"Error connecting to API: {e}")
