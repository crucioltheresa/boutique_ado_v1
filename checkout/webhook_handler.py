from django.http import HttpResponse


class StripeWH_Handler:
    """Handler Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handler_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}', status=200
        )

    def handler_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        print(intent)
        return HttpResponse(content=f'Webhook received: {event["type"]}', status=200)

    def handler_payment_intent_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(content=f'Webhook received: {event["type"]}', status=200)
