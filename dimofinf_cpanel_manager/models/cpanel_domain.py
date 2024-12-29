
import requests
from odoo import models, fields, api, exceptions

class CPanelDomain(models.Model):
    _name = 'cpanel.domain'
    _description = 'Domain Management'

    name = fields.Char(string="Domain Name", required=True)
    customer_id = fields.Many2one('res.partner', string="Customer")
    status = fields.Selection([('available', 'Available'), ('reserved', 'Reserved'), ('registered', 'Registered')], default='available', string="Status")
    registrar = fields.Char(string="Registrar", default="eNom")
    registration_date = fields.Date(string="Registration Date")
    expiry_date = fields.Date(string="Expiry Date")
    server_id = fields.Many2one('cpanel.server', string="Associated Server")

    def check_availability(self):
        """Check domain availability using eNom API."""
        enom_api_url = "https://reseller.enom.com/interface.asp"
        enom_api_key = "YOUR_ENOM_API_KEY"  # Replace with your actual eNom API Key

        payload = {
            "command": "check",
            "uid": "YOUR_ENOM_USERNAME",  # Replace with your eNom username
            "pw": enom_api_key,
            "sld": self.name.split('.')[0],
            "tld": self.name.split('.')[-1],
            "responsetype": "json"
        }

        try:
            response = requests.get(enom_api_url, params=payload)
            if response.status_code == 200:
                data = response.json()
                if data.get("RRPCode") == 210:  # Domain available
                    self.status = 'available'
                else:
                    self.status = 'reserved'
            else:
                raise exceptions.UserError(f"Failed to check domain availability: {response.text}")
        except requests.RequestException as e:
            raise exceptions.UserError(f"Error connecting to eNom API: {e}")
