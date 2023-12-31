# Generated by Django 4.2.5 on 2023-09-21 01:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('descricao', models.TextField()),
                ('dataEntrega', models.DateField()),
                ('concluida', models.BooleanField(default=False)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tarefa', to='controle.aluno')),
                ('disciplina', models.ManyToManyField(related_name='tarefa', to='controle.disciplina')),
            ],
        ),
    ]
