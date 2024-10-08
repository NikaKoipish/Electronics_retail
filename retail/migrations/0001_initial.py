# Generated by Django 5.1 on 2024-08-22 09:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="NetworkUnit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Имя")),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                ("country", models.CharField(max_length=100, verbose_name="Страна")),
                ("city", models.CharField(max_length=100, verbose_name="Город")),
                ("street", models.CharField(max_length=100, verbose_name="Улица")),
                ("house_number", models.IntegerField(verbose_name="Номер дома")),
                (
                    "level",
                    models.IntegerField(
                        choices=[
                            ("0", "завод"),
                            ("1", "розничная сеть"),
                            ("2", "индивидуальный предприниматель"),
                        ],
                        verbose_name="Уровень сети",
                    ),
                ),
                (
                    "dept",
                    models.DecimalField(
                        decimal_places=2,
                        default=0.0,
                        max_digits=15,
                        verbose_name="Задолженность перед поставщиком, руб.",
                    ),
                ),
                (
                    "date_of_create",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Время создания"
                    ),
                ),
                (
                    "supplier",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="retail.networkunit",
                        verbose_name="Поставщик",
                    ),
                ),
            ],
            options={
                "verbose_name": "Звено сети",
                "verbose_name_plural": "Звенья сети",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=250, verbose_name="Название продукта"),
                ),
                (
                    "product_model",
                    models.CharField(max_length=250, verbose_name="Модель продукта"),
                ),
                ("release_date", models.DateField(verbose_name="Дата выхода продукта")),
                (
                    "network_unit",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="retail.networkunit",
                        verbose_name="Поставщик",
                    ),
                ),
            ],
            options={
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
    ]
