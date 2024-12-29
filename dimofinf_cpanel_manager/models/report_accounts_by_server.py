
from odoo import models,fields,api,_

class CPanelAccountReportByServer(models.AbstractModel):
    _name = 'report.dimofinf_cpanel_manager.report_accounts_by_server'
    _description = 'Accounts Report by Server'

    @api.model
    def _get_report_values(self, docids, data=None):
        servers = self.env['cpanel.server'].browse(docids)
        report_data = []
        for server in servers:
            accounts = self.env['cpanel.account'].search([('server_id', '=', server.id)])
            accounts_data = []
            for account in accounts:
                accounts_data.append({
                    'name': account.name,
                    'domain': account.domain,
                    'state': account.state,
                    'customer_name': account.customer_id.name,
                    'customer_email': account.customer_id.email,
                    'customer_phone': account.customer_id.phone or 'N/A',
                })
            report_data.append({
                'server_name': server.name,
                'total_accounts': len(accounts),
                'accounts': accounts_data,
            })
        return {'doc_ids': docids, 'doc_model': 'cpanel.server', 'data': report_data}
