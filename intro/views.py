from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render


@login_required
def index(request):
    return HttpResponse('Hello, World!')


@login_required
def products(request):
    all_products = {
        'products': [
            {
                'name_of_product': 'Iphone14',
                'price': 1200,
                'year': 2022,
                'memory': '256GB'
            },
            {
                'name_of_product': 'Ipad14',
                'price': 1400,
                'year': 2021,
                'memory': '1TB'
            },
            {
                'name_of_product': 'Imac',
                'price': 3000,
                'year': 2022,
                'memory': '256GB'
            }
        ]
    }

    return render(request, 'intro/list_of_products.html', all_products)


@login_required
def songs(request):
    all_songs = {
        'songs': [
            {
                'name_of_song': 'Mistadobalina',
                'artist': 'Del the Funky Homosapien',
                'album': 'I Wish My Brother George Was Here',
                'year': 1991,
                'genre': 'Hip-Hop'
            },
            {
                'name_of_song': 'De Spus',
                'artist': 'Omu Gnom',
                'album': 'Hrana',
                'year': 2017,
                'genre': 'Hip-Hop'
            },
            {
                'name_of_song': 'Roll Play',
                'artist': 'PAWSA',
                'album': 'Roll Play',
                'year': 2017,
                'genre': 'House'
            },
            {
                'name_of_song': 'Sefu',
                'artist': 'Macanache',
                'album': 'Interzis',
                'year': 2016,
                'genre': 'Hip-Hop'
            },
            {
                'name_of_song': 'The Road',
                'artist': 'Shahmen',
                'album': 'All in the Circle (Deluxe Edition)',
                'year': 2015,
                'genre': 'Hip-Hop'
            },
            {
                'name_of_song': 'Wrong Side of Heaven',
                'artist': 'Five Finger Death Punch',
                'album': 'The Wrong Side of Heaven and the Righteous Side of Hell, Volume 1',
                'year': 2013,
                'genre': 'Metal/Rock'
            }
        ]
    }

    return render(request, 'intro/list_of_songs.html', all_songs)
