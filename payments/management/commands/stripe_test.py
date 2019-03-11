import stripe
import datetime
from django.core.management.base import BaseCommand, CommandError

from ...models import Subscription

class Command(BaseCommand):
    '''
    https://docs.djangoproject.com/en/2.1/howto/custom-management-commands/
    '''

    help = 'Print subscription information from Stripe'

    def print_tabular(self, *args):
        self.stdout.write('\t'.join(['{}'] * len(args)).format(*args))

    def handle(self, *args, **options):
        stripe.api_key = input('Stripe API key? ') # ahem, read this from the environment or something
        self.print_tabular('Email', 'Plan', 'Status', 'Last Payment')
        for subscription in Subscription.objects.all():
            customer = stripe.Customer.retrieve(subscription.custid)
            expected_amount = subscription.amount
            latest_paid_invoice = None
            if customer.subscriptions.count:
                # For someone whose payments are current, we should be able to
                # get their latest invoice without another API call
                latest_invoice = stripe.Invoice.retrieve(
                    customer.subscriptions.data[0].latest_invoice)
                if latest_invoice.amount_paid > 0:
                    latest_paid_invoice = latest_invoice
            if latest_paid_invoice is None:
                # Stripe says: "The invoices are returned sorted by creation
                # date, with the most recently created invoices appearing
                # first."
                invoices = stripe.Invoice.list(customer=subscription.custid)
                latest_invoice = invoices.data[0]
                latest_paid_invoice = None
                for invoice in invoices:
                    if invoice.amount_paid > 0:
                        latest_paid_invoice = invoice
                        break
            amount_paid = latest_paid_invoice.amount_paid
            paid_at = datetime.datetime.fromtimestamp(
                latest_paid_invoice.status_transitions.paid_at)

            if (
                    not customer.delinquent and
                    amount_paid == expected_amount and
                    datetime.datetime.now() - paid_at <=
                        datetime.timedelta(days=31)
            ):
                # TODO: check payment history?
                status = 'OK!'
            else:
                status = 'Problem'

            self.print_tabular(
                customer.email,
                subscription.plan,
                status,
                paid_at
            )
