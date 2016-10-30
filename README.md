# PlainYogurt

Getting started:
	Installs django on Ubuntu. Similar for Macs. If you're using windows... good luck

1. Install django for your environment
	https://docs.djangoproject.com/en/1.10/intro/install/
1.1 git clone git://github.com/django/django.git
1.2 sudo apt-get install python3-pip
1.3 sudo pip3 install -e django

2. Install python 3.4 (sudo apt-get install python-3.4)
3. Install MySQL (sudo apt-get install mysql-server-5.6)
4. Go into MySQL (mysql -u root -p)
5. create database (create database PYdatabase;)
6. create new user (create user 'plain' identified by 'yogurt';)
7. give plain access to database (grant all privileges on PYdatabase . * to 'plain';)
8. exit mysql (quit)

9. sudo pip3 install pymysql
10. sudo pip3 install mysqlclient

11. migrate all databases (python3 manage.py migrate)

12. run server (python3 manage.py runserver)
13. on web browser, go to localhost:8000

Note: For Windows
Install Python and MySQL: Just Google "Python windows installer"
If you meet these error: python is not a recognized as an internal or external command
... add python to PATH environment variable.
