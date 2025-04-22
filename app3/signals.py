'''
Question 3: By default do django signals run in the same database transaction as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

Solution 3: Yes, Django signals run in the same database transaction as the caller by default. This can be confirmed by observing that when a signal is triggered after a model instance is saved, it operates within the same transaction context. If the signal runs before the transaction is committed, it can access the uncommitted changes made by the caller.
'''


from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction
from .models import ImportantRecord

@receiver(post_save, sender=ImportantRecord)
def transaction_check(sender, instance, **kwargs):
    print(f"[SIGNAL] Transaction active: {not transaction.get_autocommit()}")