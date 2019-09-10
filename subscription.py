# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.

from trytond.model import fields
from trytond.pool import Pool, PoolMeta


class Subscription(metaclass=PoolMeta):
    __name__ = 'sale.subscription'
    total_discount = fields.Boolean('Total Discount')

    @staticmethod
    def default_total_discount():
        return False

    @classmethod
    def copy(cls, subscriptions, default=None):
        if default is None:
            default = {}
        else:
            default = default.copy()
        default.setdefault('total_discount', None)
        return super(Subscription, cls).copy(subscriptions, default=default)

    @classmethod
    def generate_invoice(cls, date=None):
        super(Subscription, cls).generate_invoice(date)
        Invoice = Pool().get('account.invoice')
        invoices = Invoice.search([
                ('state', '=', 'draft'),
                ('subscription_total_discount', '=', True)
                ])
        Invoice.cancel(invoices)

    def _get_invoice(self):
        invoice = super(Subscription, self)._get_invoice()
        invoice.subscription_total_discount = self.total_discount
        return invoice


class Invoice(metaclass=PoolMeta):
    __name__ = 'account.invoice'
    subscription_total_discount = fields.Boolean('Total Discount')

    @staticmethod
    def default_subscription_total_discount():
        return False
