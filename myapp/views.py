from django.shortcuts import render # type: ignore
def index_view(request):
    return render (request, 'index.html')
