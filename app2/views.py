import threading
from django.shortcuts import render
from .models import Log

def trigger_log(request):
    view_thread_id = threading.get_ident()
    print(f"[VIEW] Thread ID in view: {view_thread_id}")

    log = Log.objects.create(message="Testing thread identity")

    log._view_thread_id = view_thread_id

    return render(request, 'same_thread.html', {
        'log': log,
        'view_thread_id': view_thread_id,
        'signal_thread_id': getattr(log, '_signal_thread_id', None),
        'message': 'Thread Identity Check Completed',
    })