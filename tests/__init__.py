# The COPYRIGHT file at the top level of jhis repository contains the
# full copyright notices and license terms.

try:
    from trytond.modules.sale_subscription_total_discount.tests.test_sale_subscription_total_discount import suite
except ImportError:
    from .test_sale_subscription_total_discount import suite

__all__ = ['suite']
