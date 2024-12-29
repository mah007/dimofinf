
from odoo import models, fields, api, exceptions

class CPanelFile(models.Model):
    _name = 'cpanel.file'
    _description = 'cPanel File Management'

    path = fields.Char(string="File Path", required=True)
    size = fields.Integer(string="File Size")
    permission = fields.Char(string="Permission")
    server_id = fields.Many2one('cpanel.server', string="Server", required=True)

    def upload_file(self, file_content):
        url = f"{self.server_id.api_url}/upload_file"
        headers = {'Authorization': f"Bearer {self.server_id.api_token}"}
        payload = {'path': self.path}
        files = {'file': file_content}
        response = requests.post(url, headers=headers, data=payload, files=files)
        if response.status_code != 200:
            raise exceptions.UserError(f"Failed to upload file: {response.text}")

    def delete_file(self):
        url = f"{self.server_id.api_url}/delete_file"
        headers = {'Authorization': f"Bearer {self.server_id.api_token}"}
        payload = {'path': self.path}
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code != 200:
            raise exceptions.UserError(f"Failed to delete file: {response.text}")
