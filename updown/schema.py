import graphene
from graphene_django.types import DjangoObjectType
from django.db import models
from django.core.files.base import ContentFile
import base64


class crmDocument(models.Model):
    file = models.FileField(upload_to='crm/')

class Customer(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    documents = models.ManyToManyField(crmDocument, related_name='customers')

    def __str__(self):
        return self.name
    
class CustomerType(DjangoObjectType):
    class Meta:
        model = Customer
        fields = '__all__'
    



class Customers(graphene.ObjectType):
    pass

class DeleteCustomer(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()
    
    def mutate(self, info, id):
        instance = Customer.objects.get(pk=id)
        instance.delete()
        return DeleteCustomer(success=True)

class UpdateCustomer(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()
        email= graphene.String()
        #file_name = graphene.String()
        #file = graphene.String()  # Base64-encoded image data

    customer = graphene.Field(CustomerType)

    def mutate(self, info, id, **kwargs):
        customer = Customer.objects.get(pk=id)
        return UpdateCustomer(customer=customer)

class InsertCustomer(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        email= graphene.String()
        file_names = graphene.List(graphene.String)
        files = graphene.List(graphene.String)

    customer = graphene.Field(CustomerType)

    def mutate(self, info, **kwargs):        
        customer = Customer()
        file_names = kwargs.pop('file_names', [])
        files =kwargs.pop('files', [])
        customer = Customer( **kwargs) 
        customer.save()   
        #customer.save()  # Save the customer to generate an ID
        #file_name = str(customer.id)  Use customer's ID as the file name
        for file, file_name in zip(files, file_names):
            if file and file_name:
                image_data = base64.b64decode(file)
                document = crmDocument.objects.create(file=None)
                document.file.save(file_name, ContentFile(image_data))
                document.save()
                customer.documents.add(document)
        customer.save()
        return InsertCustomer(customer=customer)




class Query(Customers):
    pass

class Mutation(
    DeleteCustomer,
    UpdateCustomer,
    InsertCustomer,
    graphene.ObjectType):
    pass

 


schema = graphene.Schema(query=Query, mutation=Mutation)