from django.http import HttpResponse
from django.db import transaction
from django.shortcuts import render
from .models import ImportantRecord

def save_record(request):
    transaction_status = ""
    
    with transaction.atomic():
        print("[VIEW] Transaction Opened")
        ImportantRecord.objects.create(name="Test")
        print("[VIEW] Transaction Before Commit")
        transaction_status = "Record has been saved, and the transaction is still open."
    
    return render(request, 'transaction.html', {
        'transaction_status': transaction_status,
        'message': "The record was successfully created and is part of an active transaction.",
    })
