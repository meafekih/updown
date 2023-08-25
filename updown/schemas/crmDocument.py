import graphene
from graphene_django.types import DjangoObjectType
from django.db import models
from .customer import Customer

    
class crmDocument(models.Model):
    file = models.FileField(upload_to='crm/')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)

class CrmDocumentType(DjangoObjectType):
    class Meta:
        model = crmDocument


