from odoo import _, api, fields, models


class InvoicePaymentsDetail(models.Model):
    _name = 'invoice.payments.detail'
    _description = 'Invoice Payments Detail'

    move_id = fields.Many2one(
        'account.move',
        string='Move',
        required=True,
        ondelete='cascade'
    )
    journal_name = fields.Char('Journal Name')
    amount = fields.Monetary('Amount')
    currency_id = fields.Many2one(
        'res.currency',
        string='Currency',
        default=lambda self: self.env.company.currency_id.id,
        required=True
    )
    date = fields.Date('Date')
