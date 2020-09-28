from django.shortcuts import render
from django_python3_ldap.utils import format_search_filters

# Create your views here.

def custom_format_search_filters(ldap_fields):
    ldap_fields["objectCategory"] = "CN=Person,CN=Schema,CN=Configuration,DC=TESTe,DC=TESTE"
    search_filters = format_search_filters(ldap_fields)
    return search_filters
