# Generated by Django 5.1.4 on 2024-12-16 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255)),
                ('id_formation', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Eleves',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255)),
                ('prenom', models.CharField(max_length=255)),
                ('sex', models.CharField(max_length=255)),
                ('formation', models.CharField(max_length=255)),
                ('option', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Formations',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('anne_bac', models.CharField(max_length=255)),
                ('nom', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Modules',
            fields=[
                ('nom', models.CharField(max_length=255)),
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('heures', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Nouveau',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('s_et_anne', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Profs',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255)),
                ('prenom', models.CharField(max_length=255)),
                ('sex', models.CharField(max_length=255)),
                ('matiere', models.CharField(max_length=255)),
                ('contrat', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Salles',
            fields=[
                ('campus', models.CharField(max_length=255)),
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SModules',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255)),
                ('heures', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='article',
            name='reporter',
        ),
        migrations.DeleteModel(
            name='Classe',
        ),
        migrations.DeleteModel(
            name='Eleve',
        ),
        migrations.DeleteModel(
            name='Formation',
        ),
        migrations.DeleteModel(
            name='Module',
        ),
        migrations.DeleteModel(
            name='Prof',
        ),
        migrations.DeleteModel(
            name='Salle',
        ),
        migrations.DeleteModel(
            name='SModule',
        ),
        migrations.AlterField(
            model_name='calendar',
            name='id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Reporter',
        ),
    ]
