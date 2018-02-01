# flask-wtf-example

A project to illustrate a possible QuerySelectField bug in Flask-WTF when using SQLAlchemy 1.2.x


## Setup

With Python 2.7 (untested on 3.x), run:

```
virtualenv venv
. venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
FLASK_DEBUG=1 ./manage.py run
```

When visiting 127.0.0.1:5000, you should receive the "ValueError: too many values to unpack" exception. If you stop the app, downgrade SQLAlchemy from 1.2.2 to 1.1, and re-run the app, the exception is no longer raised and you should see a QuerySelectField being populated as expected.
