from odoo import _, api, fields, models



class AccountMove(models.Model):
    _inherit = 'account.move'
    _description = 'Account Move'

    invoice_payments_widget_ids = fields.One2many('invoice.payments.detail', 'move_id', string='Invoice PAyments Widget')

    def get_invoice_payments_widget_ids(self):
        for record in self:
            if record.invoice_payments_widget:
                record.invoice_payments_widget_ids.unlink()
                for payment in record.invoice_payments_widget.get('content', []):
                    values = {
                        'journal_name': payment.get('journal_name', None),
                        'amount': payment.get('amount', None),
                        'date': payment.get('date', None),
                    }
                    record.invoice_payments_widget_ids = [(0, 0, values)]
