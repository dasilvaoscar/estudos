import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class CSV(object):

    def read_csv(self):

        try:
            file = os.path.join(BASE_DIR, 'DataBase\\files\\csv.csv')
        except(Exception) as e:
            return e
        df = pd.read_csv(file)

        print(df)


var = CSV()
var.read_csv()