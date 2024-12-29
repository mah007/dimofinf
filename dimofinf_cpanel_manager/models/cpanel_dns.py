
from odoo import models, fields, api, exceptions

class CPanelDNS(models.Model):
    _name = 'cpanel.dns'
    _description = 'cPanel DNS Management'

    name = fields.Char(string="Record Name", required=True)
    type = fields.Selection([('A', 'A'), ('CNAME', 'CNAME'), ('MX', 'MX'), ('TXT', 'TXT')], string="Record Type", required=True)
    value = fields.Char(string="Value", required=True)
    domain = fields.Many2one('cpanel.account', string="Domain", required=True)

    def add_dns_record(self):
        url = f"{self.domain.server_id.api_url}/add_dns_record"
        headers = {'Authorization': f"Bearer {self.domain.server_id.api_token}"}
        payload = {
            'name': self.name,
            'type': self.type,
            'value': self.value,
            'domain': self.domain.name
        }
        try:
            response = requests.post(url, headers=headers, json=payload)
            if response.status_code != 200:
                raise exceptions.UserError("Failed to add DNS record.")
        except requests.RequestException as e:
            raise exceptions.UserError(f"Error connecting to API: {e}")
