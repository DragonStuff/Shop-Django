# Sightcorp-Django

## Generating test data

Run the following command to generate some test data. You can alter the numeric values for more or less data.

```
python manage.py loadtestdata product_manager.Product:20 product_manager.Category:3 --generate-fk category
```

