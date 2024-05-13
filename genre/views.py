from django.shortcuts import render
from django.http import JsonResponse
from genre.models import Genre
from django.views.decorators.csrf import csrf_exempt

import json

@csrf_exempt
def genre_view(request):
    if request.method == 'GET':
        genres = Genre.objects.all()
        data = []

        for genre in genres:
            data.append({'id':genre.id, 'name': genre.name})
        return JsonResponse(data, safe=False)
    
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))

        new_genre = Genre(name = data['name'])
        new_genre.save()

        return JsonResponse({'id': new_genre.id, 'name': new_genre.name}, status=201)
    