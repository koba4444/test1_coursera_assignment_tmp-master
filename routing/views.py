from django.shortcuts import render

def simple_route(request):
    return render(request, 'filters.html', context={
        'a': request.GET.get('a', 1),
        'b': request.GET.get('b', 1)
    })

def slug_route(request):
    return render(request, 'filters1.html', context={
        'a': request.GET.get('a', 1),
        'b': request.GET.get('b', 1)
    })

def sum_route(request):
    return render(request, 'filters1.html', context={
        'a': request.GET.get('a', 1),
        'b': request.GET.get('b', 1)
    })

def sum_get_method(request):
    return render(request, 'filters1.html', context={
        'a': request.GET.get('a', 1),
        'b': request.GET.get('b', 1)
    })


def sum_post_method(request):
    return render(request, 'filters1.html', context={
        'a': request.GET.get('a', 1),
        'b': request.GET.get('b', 1)
    })