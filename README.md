# Sightcorp-Django

Technologies used:

- Django
- django-autofixtures (https://github.com/gregmuellegger/django-autofixture) - For generating test data.
- Materialize CSS (https://materializecss.com/) - For template styling.

## How to use this project

This project uses Python 3 and also pip to manage dependencies.

- Clone the repository using Git.
- `pip install -r requirements.txt`
- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py runserver`

## Generating test data

Run the following command to generate some test data. You can alter the numeric values for more or less data.

```
python manage.py loadtestdata product_manager.Category:3 product_manager.Product:20
```

## Generating a superuser

Run the following command to generate a superuser. You can then log in at /admin/ to alter both Product and Category objects.

```
python manage.py createsuperuser
```
