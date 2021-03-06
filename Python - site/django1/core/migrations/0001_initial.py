# Generated by Django 3.2.6 on 2021-09-11 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50, verbose_name='Title')),
                ('Price', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Price')),
                ('Description', models.TextField(max_length=500, verbose_name='Description')),
                ('Inventory', models.IntegerField(verbose_name='Quantidade em estoque')),
            ],
        ),
    ]
