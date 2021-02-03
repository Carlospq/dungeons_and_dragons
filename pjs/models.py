from django.db import models

# Create your models here.
class Race(models.Model):
    name = models.CharField(default="", max_length=100)
    ability_score_increase = models.CharField(max_length=100)
    #age = models.IntegerField(default=0)
    #alignment = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    speed = models.IntegerField(default=20)
    languages = models.CharField(max_length=200)
    darkvision = models.BooleanField(default=True)
    descr = models.CharField(max_length=200, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Races"

    def __str__(self):
        return self.name

    def description(slef):
        return "%s %s" % (self.name, self.descr)


class SubRace(models.Model):
    name = models.CharField(max_length=100)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    subrace_ability_score_increase = models.CharField(max_length=100)
    descr = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Subraces"

    def __str__(self):
        return self.name

    def description(slef):
        return "%s %s" % (self.name, self.descr)


class Class(models.Model):
    name = models.CharField(max_length=100)
    class_level = models.IntegerField(default=1)
    hit_die = models.CharField(max_length=100)
    primary_ability = models.CharField(max_length=10)
    saving_throws = models.CharField(max_length=100)
    armor_proficiency = models.CharField(max_length=100)
    weapon_proficiency = models.CharField(max_length=100)
    descr = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Classes"

    def __str__(self):
        return self.name

    def description(slef):
        return "%s %s" % (self.name, self.descr)

class Features(models.Model):
    name = models.CharField(max_length=100)
    class_name = models.ForeignKey(Class, on_delete=models.PROTECT)
    descr = models.CharField(max_length=200, null=True, blank=True)

    class Meta: 
        verbose_name_plural = "Features"

    def __str__(self):
        return self.name

    def description(slef):
        return "%s %s" % (self.name, self.descr)