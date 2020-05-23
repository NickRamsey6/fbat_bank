import csv, io
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from .models import Statement

# Create your views here.
def index(request):
    """The home page for Bank Uploads"""
    return render(request, 'fbat_bank/index.html')

@permission_required('admin.can_add_log_entry')
def statement_upload(request):
    template = "statement_upload.html"

    prompt = {
        'order': 'Order of the CSV should be: Transaction Date, Post Date, Description, Category, Type, Amount'
    }    

    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Statement.objects.update_or_create(
            transaction_date=column[0],
            post_date=column[1],
            description=column[2],
            category=column[3],
            type=column[4],
            amount=column[5]
        )   
    context = {}
    return render(request, template, context)        