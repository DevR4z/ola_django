from django.shortcuts import render


def blog(request):
    return render(
        request,
        'blog/blog_home.html'
        )


def exemplo(request):
    return render(
        request,
        'blog/exemplo.html'
        )
