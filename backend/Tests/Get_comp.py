# run python manage.py shell
# Then exec(open('Tests/Get_comp.py').read())

from django.test import Client
import os
#import pyodbc
import numpy as np
import pandas as pd
from sqlalchemy.engine import URL
from sqlalchemy import create_engine

#import warnings
#warnings.filterwarnings('ignore')

#connection_string = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=dagger;DATABASE=test;UID=user;PWD=password"
#connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
#engine = create_engine(connection_url)

def GetListofCompetitors():
    #df = pd.read_sql_query("SELECT DISTINCT [keppandanúmer], [nafn], [dagsetning], [félag], [fæðingarár] FROM [Athletics].[dbo].[Athl$Afrek]", cnxn)
    df = pd.read_sql_query("SELECT DISTINCT [keppandanúmer], [nafn], [dagsetning], [félag], [fæðingarár] FROM [Athletics].[dbo].[Athl$Afrek]", engine)
    return df

PWD = os.environ.get('THOR_DB_PASS')
#cnxn = pyodbc.connect(r'Driver={{/opt/microsoft/msodbcsql17/lib64/libmsodbcsql-17.9.so.1.1}};SERVER=82.221.94.225;DATABASE=Athletics;UID=a;PWD={}.'.format(PWD))

print('SQL connecting')
#connection_string = r'Driver={{/usr/lib/x86_64-linux-gnu/odbc/libtdsodbc.so}};SERVER=82.221.94.225;PORT=1443;DATABASE=Athletics;UID=a;PWD={};TrustServerCertificate=yes;Encrypt=yes'.format(PWD)
connection_string = "DRIVER={{ODBC Driver 17 for SQL Server}};SERVER=82.221.94.225;PORT=1443;DATABASE=Athletics;UID=a;PWD={}".format(PWD)
print(connection_string)
connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
engine = create_engine(connection_url)
print('SQL connected')

print('Getting list of competitors')
df = GetListofCompetitors()
print('List of competitors gotten')

#cnxn.close()
engine.dispose()
print('SQL connection closed')

c = Client()
print('Starting loop')
for index, row in df.iterrows():
    CompetitorCode = row['keppandanúmer']
    response = c.get('/api/competitor/{}/'.format(CompetitorCode))

print('Loop done')