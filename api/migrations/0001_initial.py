# Generated by Django 4.1.8 on 2023-04-27 05:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateField(max_length=10)),
                ('time', models.TimeField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('id_number', models.CharField(max_length=15, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=50)),
                ('user_id', models.OneToOneField(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
                ('rating', models.CharField(max_length=100)),
                ('cita_id', models.OneToOneField(db_column='cita_id', on_delete=django.db.models.deletion.CASCADE, to='api.appointment')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('id_number', models.CharField(max_length=15, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=50)),
                ('user_id', models.OneToOneField(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='appointment',
            name='doctor_id',
            field=models.ForeignKey(db_column='doctor_id', on_delete=django.db.models.deletion.CASCADE, to='api.doctor', to_field='user_id'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient_id',
            field=models.ForeignKey(db_column='patient_id', on_delete=django.db.models.deletion.CASCADE, to='api.patient', to_field='user_id'),
        ),
    ]
