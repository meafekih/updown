
import graphene
from updown.queries import (Customers, Documents, )
from updown.mutations import (DeleteCustomer, UpdateCustomer,
    InsertCustomer, )




class Query(Customers,Documents):
    pass

class Mutation(graphene.ObjectType):
    deleteCustomer = DeleteCustomer.Field()
    updateCustomer = UpdateCustomer.Field()
    insertCustomer = InsertCustomer.Field()
    


schema = graphene.Schema(query=Query, mutation=Mutation)