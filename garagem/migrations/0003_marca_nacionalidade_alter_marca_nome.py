# Generated by Django 4.1.7 on 2023-03-13 19:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("garagem", "0002_alter_marca_nome"),
    ]

    operations = [
        migrations.AddField(
            model_name="marca",
            name="nacionalidade",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="marca",
            name="nome",
            field=models.CharField(max_length=50),
        ),
    ]
