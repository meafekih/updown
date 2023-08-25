import graphene
from .schemas.customer import Customer, CustomerType
from .schemas.crmDocument import crmDocument



class Documents(graphene.ObjectType):
    documents = graphene.List(graphene.String, customer_id=graphene.Int())

    def resolve_documents(self, info, customer_id):
        try:
            customer = Customer.objects.get(pk=customer_id)
            docs = crmDocument.objects.filter(customer=customer)
            return [doc.file.url for doc in docs]
        except Customer.DoesNotExist:
            return []




class Customers(graphene.ObjectType):
    customers = graphene.List(CustomerType)

    def resolve_customers(self, info,  **kwargs):
        customs = Customer.objects.all()
        return customs
   