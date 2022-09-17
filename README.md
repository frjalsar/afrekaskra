# Afrekaskrá FRÍ

## How-to:
0. Install Python 3.10 or higher.
1. sudo apt install libpq-dev unixodbc-dev libsqliteodbc tdsodbc python3-dev npm git build-essentials
2. git clone
3. npm install
4. npm run build
5. python3 -m venv env
6. source env/bin/activate
7. pip install -r requirements.txt
8. Set the env vars 'SIF_SECRET_KEY', 'SIF_DB_USER' and 'SIF_DB_PASSWORD'
9. Create a symlink for .apt/usr/lib/x86_64-linux-gnu/odbc/libtdsodbc.so to /usr/lib/x86_64-linux-gnu/odbc/libtdsodbc.so
10. python manage.py runserver
