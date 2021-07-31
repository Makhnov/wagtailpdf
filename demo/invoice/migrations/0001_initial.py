# Generated by Django 3.2.3 on 2021-07-30 08:02

import datetime
from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail_pdf_view.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField(default=datetime.datetime.now)),
                ('address', models.TextField(max_length=500)),
                ('due_by_date', models.DateField()),
                ('account_number', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail_pdf_view.mixins.PdfModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='InvoiceItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=500)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('quantity', models.IntegerField()),
                ('invoice', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='invoice.invoice')),
            ],
        ),
    ]
