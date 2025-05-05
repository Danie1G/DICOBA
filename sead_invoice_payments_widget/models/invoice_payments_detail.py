from odoo import _, api, fields, models


class InvoicePaymentsDetail(models.Model):
    _name = 'invoice.payments.detail'
    _description = 'Invoice Payments Detail'

    move_id = fields.Many2one('account.move', string='Move')
    journal_name = fields.Char('Journal Name')
    amount = fields.Float('amount')
    date = fields.Date('date')
