from django.db import migrations, models
from django.conf import settings
import os
import csv
import datetime

def load_books (apps, schema_editor):
    Book = apps.get_model('core', 'Book')

    Book.objects.all().delete()


    filename = os.path.join(settings.BASE_DIR, 'sample_books.csv')

    with open(filename) as file:
        reader = csv.DictReader(file)
        for row in reader:
            book = Book (
                title = row['title'],
                author = row['author'],
                url = row['url'],
                description = row['description'],
                date_added = datetime.datetime.now()
                )
            book.save()


def delete_data(apps, schema_editor):
    Book = apps.get_model('core', 'Book')
    

    Book.objects.all().delete()
    


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [migrations.RunPython(load_books, delete_data)]