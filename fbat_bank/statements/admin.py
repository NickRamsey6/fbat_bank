from django.contrib import admin

# Register your models here.
from statements.models import Transaction

admin.site.register(Transaction)