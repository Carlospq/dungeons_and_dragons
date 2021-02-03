from django.db import models
from django.utils import timezone
import datetime

## To remmeber:
#    def set_languages(self, x):
#        self.foo = json.dumps(x)
#
#    def get_languages(self):
#        return json.loads(self.foo)


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Race(models.Model):
    name = models.CharField(max_length=100)
    #CON2+ // CON1-
    ability_score_increase = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    alignment = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    speed = models.IntegerField(default=20)
    languages = models.CharField(max_length=200)
    subraces = models.CharField(max_length=100)
    darkvision = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def name(self):
        return self.name


class SubRace(models.Model):
    name = models.CharField(max_length=100)
    race = models.CharField(max_length=100)
    subrace_ability_score_increase = models.CharField(max_length=100)



#import csv, os, json
#with open('./data/races.csv') as f:
#    h=0
#    reader = csv.reader(f, delimiter = '\t')
#    for row in reader:
#        if h == 0:
#            header = row
#            h += 1
#            continue
#        _, created = Race.objects.get_or_create(
#        name = row[0],
#        ability_score_increase = row[1],
#        age = row[2],
#        alignment = row[3],
#        size = row[4],
#        speed = row[5],
#        languages = row[6],
#        subraces = row[7],
#        darkvision = row[8])   




#for file in os.listdir('./data/'):
#    h = 0
#    with open('./data/races.csv') as f:
#       reader = csv.reader(f, delimiter = '\t')
#        for row in reader:
#            if h == 0:
#                header = row
#                h += 1
#                continue
#            #d = {}
#            #for i in range(0, len(header)):
#            #    d[header[i]] = row[i]
#            #json_d = json.dumps(d)
#            #_, created = Race.objects.get_or_create(d)
#            _, created = Race.objects.get_or_create(
#            name = row[0],
#            ability_score_increase = row[1],
#            age = row[2],
#            alignment = row[3],
#            size = row[4],
#            speed = row[5],
#            languages = row[6],
#            subraces = row[7],
#            darkvision = row[8])   

