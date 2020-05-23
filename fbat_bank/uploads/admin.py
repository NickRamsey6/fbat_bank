from django.contrib import admin

# Register your models here.
from uploads.models import Statement, Transaction

admin.site.register(Statement)
admin.site.register(Transaction)