from django.shortcuts import render


def home(request):
    print('Home')

    context = {
        'text': 'Home Page'
    }

    return render(
        request,
        'home/index.html',
        context,
    )
