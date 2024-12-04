from django.shortcuts import render
from .models import Streets, FirstNames, Otchs, Surnames, Main
import json
import random

# Create your views here.


def index(request):

    with open('first_names.json', encoding='utf-8') as file:
        first_names = []
        for i in file.readlines():
            if len(i) > 5:
                first_names.append(json.loads(i[2:-2]))

    with open('surnames.json', encoding='utf-8') as file:
        surnames = []
        for i in file.readlines():
            if len(i) > 5:
                surnames.append(json.loads(i[2:-2]))

    with open('otchs.json', encoding='utf-8') as file:
        otchs = []
        for i in file.readlines():
            if len(i) > 5:
                otchs.append(json.loads(i[2:-2]))

    n = 89000000000

    for i in range(500):
        f_name = random.randint(0, len(first_names) - 1)
        sur = random.randint(0, len(surnames) - 1)
        o = random.randint(0, len(otchs) - 1)
        street = random.randint(1, 20)
        if surnames[sur]['g'] == first_names[f_name]['g']:
            surname = sur
        else:
            if sur % 2 == 0:
                surname = sur + 1
            else:
                surname = sur - 1

        if otchs[sur]['g'] == otchs[f_name]['g']:
            otch = o
        else:
            if o % 2 == 0:
                otch = o + 1
            else:
                otch = o - 1

        Main(house=str(random.randint(1, 10)),
             corpus=str(random.randint(1, 2)),
             apart=str(random.randint(1, 50)),
             tel=str(n),
             surname_fk=Surnames.objects.get(id=surname+1),
             f_name_fk=FirstNames.objects.get(id=f_name+1),
             otch_fk=Otchs.objects.get(id=otch+1),
             street_fk=Streets.objects.get(id=street+1)).save()
        n += 1

    context = {'s': Streets.objects.all()}
    return render(request, 'main/index.html', context)
