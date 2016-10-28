# PlainYogurt

Getting started:
1. https://docs.djangoproject.com/en/1.10/intro/install/
	Installs django on Ubuntu. Similar for Macs. If you're using windows... good luck

1.1 git clone from our repo
2. cd MainProject
3. python manage.py runserver (might need to use python3 manange.py runserver if your default python is 2.7)
4. On web browser, go to http://127.0.0.1:8000 (local host port 8000) to see website

Setting up database:
1. Install Mysql v5.5 or up
2. Log into mysql using root (mysql -u root -p)
2.1 create database (create database PYdatabase;)
3. create new user (create user 'plain' identified by 'yogurt')
3.1 give plain access to database (grant all privileges on PYdatabase . * to 'plain')
4. exit mysql


