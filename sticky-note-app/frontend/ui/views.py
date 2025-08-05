import requests
from django.shortcuts import render, redirect

API_BASE = 'http://backend:8001/api/notes/'  # lien vers le microservice backend via Docker

def index(request):
    response = requests.get(API_BASE)
    notes = response.json()
    return render(request, 'index.html', {'notes': notes})

def create_note(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        requests.post(API_BASE, data={'title': title, 'content': content})
    return redirect('index')

def delete_note(request, note_id):
    requests.delete(f"{API_BASE}{note_id}/")
    return redirect('index')
