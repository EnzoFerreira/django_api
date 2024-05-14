from django.shortcuts import render
from django.http import JsonResponse
from genre.models import Genre
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

import json

@csrf_exempt
def genre_list(request):
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
    
    
@csrf_exempt
def genre_detail(request, pk):
    genre = get_object_or_404(Genre, pk = pk)

    if request.method == 'GET':
        data = {'id': genre.id, 'name': genre.name}

        return JsonResponse(data)

    if request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8'))
        genre.name = data['name']
        genre.save()

        return JsonResponse({'id': genre.id, 'name': genre.name}, status=201)
    
    if request.method == 'DELETE':
        genre.delete()
        return JsonResponse({'message':'Genre deleted!'}, status=204)