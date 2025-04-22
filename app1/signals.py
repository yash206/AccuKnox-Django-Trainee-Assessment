'''
Question 1: By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

Solution 1: Before jumping into the question, let me first explain Django Signals from my pov.
Django Signals operate based on the sender-receiver model. They provide a mechanism for certain senders to notify a set of receivers when a specific action is performed. If we relate this to a design pattern, Django Signals closely resemble the Observer Design Pattern, where decoupled components can communicate without having direct dependencies on each other.

Django Signals typically involve three components:
Event - the condition that triggers the signal (e.g., object creation or update),
Sender - the source that triggers the condition,
Receiver - the function or method that responds to the signal.

Now, coming back to the original question:
Are Django signals executed synchronously or asynchronously by default?

By default, Django signals are executed synchronously. This is evident in how signals like pre_save, post_save, pre_delete, and post_delete behave, they are executed either just before or just after a model's save() or delete() operations. The synchronous nature ensures that the receiver logic runs as part of the same execution flow, making the timing of actions predictable and consistent with the model operations.
'''



from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order
import time

@receiver(post_save, sender=Order)
def order_confirmation(sender, instance, created, **kwargs):
    if created:
        start_time = time.time()
        print(f"New Order Created: {instance.customer_name} - {instance.product_name}")
        print(f"Processing order... (This might take a few seconds)")

        time.sleep(5)  # Delay in order processing

        print(f"Order for {instance.customer_name} - {instance.product_name} processed.")
        end_time = time.time()
        print(f"Time taken to process the order: {end_time - start_time:.2f} seconds")
