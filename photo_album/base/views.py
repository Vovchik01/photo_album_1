from django.shortcuts import render, redirect
from .models import *


def index(request):
    category = request.GET.get('category')
    if category is None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)

    categories = Category.objects.all()

    context = {'categories': categories, 'photos': photos}
    return render(request, 'base/index.html', context=context)


def view_photo(request, pk):
    photo = Photo.objects.get(id=pk)
    context = {'photo': photo}
    return render(request, 'base/view_photo.html', context=context)


def add_photo(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None

        photo = Photo.objects.create(
            category=category,
            description=data['description'],
            image=image,
        )

        return redirect('index')

    context = {'categories': categories, }
    return render(request, 'base/add_photo.html', context=context)
