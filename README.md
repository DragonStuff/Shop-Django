# Sightcorp-Django

Technology used:

- Django
- django-autofixtures (https://github.com/gregmuellegger/django-autofixture) - For generating test data.
- Materialize CSS - For template styling.

## Generating test data

Run the following command to generate some test data. You can alter the numeric values for more or less data.

```
python manage.py loadtestdata product_manager.Category:3 product_manager.Product:20
```

