from sqlalchemy import create_engine
import pandas.io.sql as psql
import os
local = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Conexao():
    def CreateConnection(self):
        try:
            self.db_conn = create_engine('mysql+mysqldb://root:Kaka25780@127.0.0.1/my_sql_test')
        except(Exception) as e:
            print('Erro na conexão com o Banco: ' + e)

        query = 'SELECT * FROM filme'

        try:
            df = psql.read_sql(query, con=self.db_conn)
            return df
        except(Exception) as e:
            print('Erro ao executar 1° Query ' + e)


class Geradores(Conexao):
    def GenerateCSV(self):

        try:
            df = self.CreateConnection()
            df.to_csv(os.path.join(local, 'DataBase\\files\\csv.csv'))
            print('CSV Gerado')
        except(Exception) as e:
            print(e)

    def GeradorExcel(self):
        try:
            df = self.CreateConnection()
            df.to_excel(os.path.join(local, 'DataBase\\files\\Excel.xlsx'))
            print('Excel Gerado')
        except(Exception) as e:
            print(e)

    def GeradorHTML(self):
        try:
            df = self.CreateConnection()
            df.to_html(os.path.join(local, 'DataBase\\files\\index.html'), classes='table')
            print('HTML Gerado')
        except(Exception) as e:
            print(e)


conection = Conexao()
conection.CreateConnection()

gerador = Geradores()
gerador.GenerateCSV()
gerador.GeradorExcel()
gerador.GeradorHTML()

