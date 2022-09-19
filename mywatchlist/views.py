from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

def show_watchlist(request):
    return render(request, "empty.html")

def show_html(request):
    watchlist_data = MyWatchList.objects.all()
    watched, not_watched = 0, 0
    for movie in watchlist_data:
        if movie.watched:
            watched += 1
        else:
            not_watched += 1

    context = {
        'list_watchlist': watchlist_data,
        'watched': watched,
        'not_watched': not_watched
    }
    return render(request, "watchlist.html", context)

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")