'''
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import *
from django.contrib.auth.models import *
import pandas as pd
import pandas.io.sql as psql
import pymysql

class Conexao(object):

    def __init__(self, query, nome_arquivo):
        self.query = query
        self.nome_arquivo = nome_arquivo

    def CreateConnection(self):
        try:
            db_conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='0sc@r@%&*)', db='intranet')
        except Exception as e:
            return HttpResponse(e)

        try:
            df = psql.read_sql(self.query, con=db_conn)
            return df
        except Exception as e:
            return HttpResponse(e)


# Create your views here.
'''