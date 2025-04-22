'''
Question 2: Do django signals run in the same thread as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

Solution 2: Yes, Django signals execute synchronously in the same thread as the caller. When a signal is sent, all connected receiver functions run immediately in sequence, blocking the main thread until completion. This synchronous behavior ensures predictable execution order but can cause performance issues if receivers perform slow operations. The signal's thread dependency is intentional for database transaction consistency.
'''

import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Log

@receiver(post_save, sender=Log)
def log_signal_thread_info(sender, instance, created, **kwargs):
    if created:
        signal_thread_id = threading.get_ident()
        print(f"[SIGNAL] Thread ID in signal: {signal_thread_id}")
        instance._signal_thread_id = signal_thread_id