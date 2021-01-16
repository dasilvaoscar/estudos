import mysql.connector

class DataBase(object):
  """ 
    Inicialização da classe de conexão
    ao banco
  """
  def __init__(self, db_name):
    self._host = "localhost"
    self._user = "root"
    self._pass = "123456"
    self._db = db_name

  def getConnection(self):
    mydb = mysql.connector.connect(
      host=self._host,
      user=self._user,
      password=self._pass,
      database=self._db
    )
    return mydb

class Repository(object):
  """ 
    Os IFs iniciáis são checagens de tipo
    para que não seja possível a quebra das
    funções
  """

  def __init__(self, db_name: str):
    self._db = DataBase(db_name)
    self._conn = self._db.getConnection()

  def createDataBase(self, db_name: str):

    if isinstance(db_name, str):
      cursor = self._conn.cursor()
      try:
        cursor.execute('CREATE DATABASE %s'%(db_name))
      except Exception as e:
        raise e
      return "Banco criado"
    else: 
      raise 'db_name deve ser String'
  
  def createTable(self, tb_name: str, tb_columns: dict):
    """ 
      tb_coluns deve ser um dicionário, onde a chave seria o nome 
      da coluna e o valor os atributos da coluna
    """
    
    if isinstance(tb_name, str) and isinstance(tb_columns, dict) == True:
      cursor = self._conn.cursor()

      re = []
      for col in zip(tb_columns.keys(), tb_columns.values()):
        re.append(' '.join(col))
      columns = ', '.join(re)

      sql = "CREATE TABLE `%s` (%s) "%(tb_name, columns)
      try:
        cursor.execute(sql)
      except Exception as e:
        raise e
      return 'Tabela criada'
    else:
      raise 'Tipos dos atributos não foram respeitados'

  def selectAll(self, tb_name: str):
    cursor = self._conn.cursor() 

    if isinstance(tb_name, str):
      try:
        cursor.execute('SELECT * FROM `%s`'%(tb_name))
      except Exception as e:
        raise e

      re = []
      for data in cursor.fetchall():
        re.append(data)
      
      return re
    else:
      raise "Tipo da variável tb_name dever ser String"
    
  def insert(self, tb_name: str, tb_columns: list, insert_values: tuple):
    cursor = self._conn.cursor()

    if isinstance(tb_name, str) and isinstance(tb_columns, list) and isinstance(insert_values, tuple):
      columns = ', '.join(tb_columns)
      values = str(insert_values).replace('(', '').replace(')', '')
      sql = "INSERT INTO %s (%s) VALUES (%s)"%(tb_name, columns, values)

      try:
        cursor.execute(sql)
        self._conn.commit()
      except Exception as e:
        raise e
      return cursor.rowcount
    else:
      raise 'Tipos dos atributos não foram respeitados' 

  def update(self, tb_name: str, set: dict, whare: dict):
    cursor = self._conn.cursor()

    set_re = []
    for set in zip(set.keys(), set.values()):
      re = "{0}='{1}'".format(set[0], set[1])
      set_re.append(re)
    set = ', '.join(set_re)

    where_re = []

    for key, data in whare.items():

      if 'condicional' in data:
        if data['condicional'] == 'or':
          re = "{0}='{1}' OR".format(key, data['value'])
          where_re.append(re)
        if data['condicional'] == 'and':
          re = "{0}='{1}' AND".format(key, data['value'])
          where_re.append(re)
      else:
        re = "{0}='{1}'".format(key, data['value'] or data)
        where_re.append(re)
      
    where_re = ', '.join(where_re)

    sql = "UPDATE %s SET %s WHERE (%s)"%(tb_name, set, where_re)
    print(sql)
    try:
      cursor.execute(sql)
      self._conn.commit()
    except Exception as e:
      raise e
    return '{0} linhas afetadas'.format(cursor.rowcount)

  def delete(self, id):
    cursor = self._conn.cursor()
    pass

repo = Repository('test_python')
#repo.createDataBase('test_python')
#repo.createTable('tab_test', {
#  'col1': 'int not null primary key auto_increment',
#  'col2': 'varchar(255)',
#  'col3': 'varchar(255)',
#  'col4': 'varchar(255)',
#  'col5': 'varchar(255)',
#})
#repo.insert('tab_test', ['col2', 'col3', 'col4', 'col5'], ('2', '3', '4', '5'))
#repo.selectAll('tab_test')
repo.update(
  'tab_test',
  {'col5': 'value'},
  {'col1':{
    'value': '1',
    'condicional': 'and'
  },
  'col1': {
    'value': '1'
  }
  }
)