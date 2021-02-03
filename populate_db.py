import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','dungeons_and_dragons.settings')

import django
django.setup()

from pjs.models import Race, SubRace, Class

def add_data(Model, data1, data2):
    d, created = Model.objects.get_or_create(data1=data1, data2=data2)
    print("- Data: {0}, Created: {1}".format(str(d), str(created)))
    return d


def populate(Model, data):
	with open(data) as f:
		rows = f.readlines()
		header = rows[0].strip().split("\t")
		d = {}
		for i in range(1,len(rows)):
			for j in range(0,len(header)):
				row = rows[i].strip("\n").split("\t")
				d[header[j]] = row[j]
			_, created = Model.objects.get_or_create(**d)

def populate_fk(Model, data, fk_model, fk_field):
	with open(data) as f:
		rows = f.readlines()
		header = rows[0].strip().split("\t")
		d = {}
		for i in range(1,len(rows)):
			for j in range(0,len(header)):
				row = rows[i].strip("\n").split("\t")
				if header[j] == fk_field:
					d[header[j]] = Race.objects.get(name=row[j])
				else:
					d[header[j]] = row[j]
			_, created = Model.objects.get_or_create(**d)

if __name__ == "__main__":
    populate(Race, './data/races.csv')
    populate_fk(SubRace, './data/subraces.csv', Race, "race")
    populate(Class, './data/classes.csv')