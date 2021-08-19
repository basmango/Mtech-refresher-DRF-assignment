# Refresher module assignment

A simple API and assignment given for a python refresher module made using django rest framework. 

## How to Use

To use this project, follow these steps:

1. Add heroku db credentials.
2. Populate with dummy data via mockaroo
2. Deploy to heroku

## Demo
http://www.basmango.com/


## Deployment to Heroku

    $ git init
    $ git add -A
    $ git commit -m "Initial commit"

    $ heroku create
    $ git push heroku master

    $ heroku run python manage.py migrate
 deploy.


## License: MIT

Made with the help of https://github.com/heroku/heroku-django-template

## Further Reading

- [Gunicorn](https://warehouse.python.org/project/gunicorn/)
- [WhiteNoise](https://warehouse.python.org/project/whitenoise/)
- [dj-database-url](https://warehouse.python.org/project/dj-database-url/)
