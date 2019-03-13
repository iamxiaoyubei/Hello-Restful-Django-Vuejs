# Hello-Django-Vuejs

## Environments
Please install python3.7.2 with pip and then run:

`pip install requirements.txt`

Open your MySQL database and change your database password in mysite/mysite/settings.py

Then you can run with:

`python manage.py runserver`

in the mysite/ dir(where you can find manage.py).

Everytime you `git pull` the newest code, please run:

`python manage.py makemigrations`
`python manage.py migrate`

to refresh database.

@苑珍，请于[API文档](./API.md)查看API
苑珍你可以用于调试

## REFERENCE:

自强学堂BVDN教程：https://code.ziqiangxuetang.com/django/bvdn7-migrate-db-mysql.html

http://www.bubuko.com/infodetail-2982730.html

mysqldb driver:https://pypi.org/project/mysqlclient/

谷歌API教程：http://www.runoob.com/googleapi/googleapi-tutorial.html
https://www.jianshu.com/p/6187d5915f70


前端也需要学习调用API：http://www.runoob.com/googleapi/google-maps-api-key.html

谷歌API文档：https://developers.google.com/maps/documentation/javascript/tutorial?hl=zh_CN

更改数据库表格：https://docs.djangoproject.com/en/2.1/topics/db/models/