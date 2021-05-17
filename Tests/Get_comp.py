# run python manage.py shell
# Then exec(open('Tests/Get_comp.py').read())

from django.test import Client
import os
import pyodbc
import numpy as np
import pandas as pd

def GetListofCompetitors():
    df = pd.read_sql_query("SELECT DISTINCT [keppandanúmer], [nafn], [dagsetning], [félag], [fæðingarár] FROM [Athletics].[dbo].[Athl$Afrek]", cnxn)
    return df

PWD = os.environ.get('THOR_DB_PASS')
cnxn = pyodbc.connect(r'Driver={{/opt/microsoft/msodbcsql17/lib64/libmsodbcsql-17.7.so.2.1}};SERVER=82.221.94.225;DATABASE=Athletics;UID=a;PWD={}.'.format(PWD))

df = GetListofCompetitors()

cnxn.close()

c = Client()
print('Starting loop')
for index, row in df.iterrows():
    CompetitorCode = row['keppandanúmer']
    response = c.get('/api/competitor/{}/'.format(CompetitorCode))

print('Loop done')
