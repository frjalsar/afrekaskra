nohup gunicorn Sif.wsgi &
echo "HELLO"
nginx -c /app/config/gunicorn.conf.py
