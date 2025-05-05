from odoo import api, fields, models
import json
from datetime import datetime
import logging

_logger = logging.getLogger(__name__)


class AccountMove(models.Model):
    _inherit = 'account.move'

    invoice_payments_widget_ids = fields.One2many(
        'invoice.payments.detail', 'move_id', string='Invoice Payments Widget'
    )

    def get_invoice_payments_widget_ids(self):
        for record in self:
            try:
                payments = json.loads(record._get_payment_info_JSON())
            except Exception as e:
                _logger.warning(f"Error parsing payment JSON for move {record.id}: {e}")
                continue

            # Clean existing records
            record.invoice_payments_widget_ids.unlink()

            all_values = []
            for payment in payments.get('content', []):
                try:
                    values = {
                        'journal_name': payment.get('journal_name'),
                        'amount': payment.get('amount'),
                        'date': datetime.strptime(payment.get('date'), '%Y-%m-%d').date()
                        if payment.get('date') else None
                    }
                    all_values.append((0, 0, values))
                except Exception as e:
                    _logger.warning(f"Invalid payment entry: {payment}, error: {e}")

            record.invoice_payments_widget_ids = all_values

