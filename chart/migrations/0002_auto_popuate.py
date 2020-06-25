import csv
import os
from django.db import migrations
from django.conf import settings


Date = 0
Country = 1
Confirmed = 2
Recovered = 3
Deaths = 4


def add_Covid(apps, schema_editor):
    Covid = apps.get_model('chart', 'Covid')
    csv_file = os.path.join(settings.BASE_DIR, 'countries-aggregated.csv')
    with open(csv_file) as dataset:
        reader = csv.reader(dataset)
        next(reader)
        for entry in reader:
            Covid.objects.create(
                date=entry[Date],
                country=entry[Country],
                confirmed=int(entry[Confirmed]),
                recovered=int(entry[Recovered]),
                deaths=int(entry[Deaths]),
            )

class Migration(migrations.Migration):
    dependencies = [
        ('chart','0001_initial'),
    ]
    operations = [
        migrations.RunPython(add_Covid),
    ]