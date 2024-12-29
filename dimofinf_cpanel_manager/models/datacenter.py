
from odoo import models, fields, api, exceptions
import requests

class DataCenter(models.Model):
    _name = 'cpanel.datacenter'
    _description = 'Data Center Management'

    name = fields.Char(string="Data Center Name", required=True)
    location = fields.Char(string="Location")
    api_url = fields.Char(string="API URL", required=True)
    api_token = fields.Char(string="API Token", required=True)
    servers = fields.One2many('cpanel.server', 'datacenter_id', string="Servers")

    def fetch_servers(self):
        """Fetch servers from the Data Center API."""
        headers = {'Authorization': f"Bearer {self.api_token}"}
        try:
            response = requests.get(f"{self.api_url}/servers", headers=headers)
            if response.status_code == 200:
                server_data = response.json()
                for server in server_data.get('servers', []):
                    existing_server = self.env['cpanel.server'].search([('name', '=', server['name'])])
                    if not existing_server:
                        self.env['cpanel.server'].create({
                            'name': server['name'],
                            'datacenter_id': self.id,
                            'api_url': server['api_url'],
                            'api_token': server.get('api_token', ''),
                        })
            else:
                raise exceptions.UserError(f"Failed to fetch servers: {response.text}")
        except requests.RequestException as e:
            raise exceptions.UserError(f"Error connecting to Data Center API: {e}")
