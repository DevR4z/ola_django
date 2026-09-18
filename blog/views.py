from django.shortcuts import render


def blog(request):
    context = {
            'text': 'Blog Page'
        }

    return render(
        request,
        'blog/blog_home.html',
        context,
        )


def exemplo(request):
    context = {
            'text': 'Exemplo Page'
        }

    return render(
        request,
        'blog/exemplo.html',
        context
        )
