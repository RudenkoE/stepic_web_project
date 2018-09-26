sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
sudo ln -s /home/box/web/etc/gunicorndjango.conf /etc/gunicorn.d/testdj
sudo /etc/init.d/gunicorn restart
sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE DATABASE qabase;"
mysql -uroot -e "CREATE USER 'qauser'@'localhost' IDENTIFIED BY '123456';"
mysql -uroot -e "GRANT ALL ON qabase.* TO 'qauser'@'localhost';"
