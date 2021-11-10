# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.

from trytond.pool import Pool
from . import subscription


def register():
    Pool.register(
        subscription.Subscription,
        subscription.Invoice,
        module='sale_subscription_total_discount', type_='model')
