import sqlalchemy
from dask.utils import insert
from sqlalchemy import create_engine, text
from pandas import DataFrame
engine = create_engine('sqlite:///1st_sqlite.sqlite3') # connection string
# 'sqlite -> dilectsqlalchemy
# engine as DB
# Relative Path -> نسبة لوين انا موجود
# absolute path -> نسبة لموقعها ع الجهاز
# sqlite:///D:\sql_pycharm\\the fisrt session sql\\1st_sqlite.sqlite3


# for select statment
ide, namee = int(input("enter id")), input("enter name")
#sql_statment = 'create table another_tables(id number(12), name varchar(255))'
sql_input =' insert into another_tables values (:id, :name) '
with engine.connect () as connection :
  connection.execute(text(sql_input),{'id' : ide, 'name' : namee })

with engine.connect () as connection :

  result_proxy =  connection.execute(text('SELECT * FROM test1 WHERE course = :course'),{'course': 'IT'} )
  # proxy is intermediate bet UI and DB and as an obj
  result_data = result_proxy.fetchall() # retrieve all data
  print(result_data)
  # each row in db is a tuple i the list
  coulmns = result_proxy.keys() # retrieve the attr
  #print(result)
  #print(coulmns)
  df = DataFrame(result_data)
  df.columns = coulmns
  print(df)



with engine.connect() as connection :
  result_proxxy =  connection.execute(text('SELECT MIN(test) FROM test1'))
  result_dataa = result_proxxy.fetchall()
  result_columns = result_proxxy.keys()
  #print(result_dataa, result_columns)
  print(result_dataa[0][0])