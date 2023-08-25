from graphene_django.types import DjangoObjectType
from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)

    def __str__(self):
        return self.name
    
class CustomerType(DjangoObjectType):
    class Meta:
        model = Customer
        fields = '__all__'
    

