
from django.urls import path
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from .schema import schema
from django.shortcuts import render, redirect

def customer_view(request):
    return render(request, 'index.html')

urlpatterns = [
    path('api/', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema)), name='api'),
    path('customers', customer_view)
]
