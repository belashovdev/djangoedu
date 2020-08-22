from django.shortcuts import render
import datetime

def home(request):
    date = datetime.datetime.now()
    name = "Pidor"

    cont = {'date': date, 'name': name}
    return render(request, 'home.html', cont)
