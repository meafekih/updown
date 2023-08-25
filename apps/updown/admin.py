from django.contrib import admin
from .schemas.customer import Customer
from .schemas.crmDocument import crmDocument


admin.site.register(crmDocument)
admin.site.register(Customer)
