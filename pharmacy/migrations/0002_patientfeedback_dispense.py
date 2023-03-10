# Generated by Django 4.1.6 on 2023-02-24 04:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientFeedback',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('feedback', models.TextField(null=True)),
                ('feedback_reply', models.TextField(null=True)),
                ('admin_created_at', models.DateTimeField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('admin_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pharmacy.adminhod')),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacy.patients')),
                ('pharmacist_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pharmacy.pharmacist')),
            ],
        ),
        migrations.CreateModel(
            name='Dispense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dispense_quantity', models.PositiveIntegerField(default='1', null=True)),
                ('taken', models.CharField(blank=True, max_length=300, null=True)),
                ('stock_ref_no', models.CharField(blank=True, max_length=300, null=True)),
                ('instructions', models.TextField(max_length=300, null=True)),
                ('dispense_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('drug_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pharmacy.stock')),
                ('patient_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pharmacy.patients')),
            ],
        ),
    ]
