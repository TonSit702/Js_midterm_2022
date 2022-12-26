# Generated by Django 4.1.3 on 2022-12-18 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('simfood', '0002_allmenu_delete_allproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catname', models.CharField(default='allmenu', max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='allmenu',
            name='catname',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='simfood.category'),
        ),
    ]