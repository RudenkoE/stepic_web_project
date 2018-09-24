sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test

sudo /etc/init.d/gunicorn restart
sudo ln -sf /home/box/web/etc/django_conf.py /etc/gunicorn.d/django_conf.py
sudo gunicorn -c /home/box/web/etc/gunicorn.conf hello:wsgi_application         
sudo gunicorn -c /home/box/web/etc/django_gunicorn.conf ask.wsgi:application
