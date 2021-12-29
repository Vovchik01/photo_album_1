from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'base/index.html', context=context)


def view_photo(request, pk):
    context = {}
    return render(request, 'base/view_photo.html', context=context)


def add_photo(request):
    context = {}
    return render(request, 'base/add_photo.html', context=context)
