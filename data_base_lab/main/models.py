from django.db import models

# Create your models here.


class FirstNames(models.Model):
    f_name = models.CharField(max_length=100)

    class Meta:
        managed = True


class Main(models.Model):
    house = models.CharField(blank=True, null=True)
    corpus = models.CharField(max_length=100)
    apart = models.CharField(blank=True, null=True)
    tel = models.CharField(max_length=50, blank=True, null=True)
    surname_fk = models.ForeignKey('Surnames', models.DO_NOTHING, db_column='surname_fk', blank=True, null=True)
    f_name_fk = models.ForeignKey(FirstNames, models.DO_NOTHING, db_column='name_fk', blank=True, null=True)
    otch_fk = models.ForeignKey('Otchs', models.DO_NOTHING, db_column='otch_fk', blank=True, null=True)
    street_fk = models.ForeignKey('Streets', models.DO_NOTHING, db_column='street_fk', blank=True, null=True)

    class Meta:
        managed = True


class Otchs(models.Model):
    otch = models.CharField(max_length=100)

    class Meta:
        managed = True


class Streets(models.Model):
    street = models.CharField(max_length=100)

    class Meta:
        managed = True


class Surnames(models.Model):
    surname = models.CharField(max_length=100)

    class Meta:
        managed = True
