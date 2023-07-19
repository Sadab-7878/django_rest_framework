from django.http import HttpResponse, JsonResponse


def homepage(request):
    print("Home Page Loading....")
    friends=[
        'Sadab',
        'Hafiz',
        'Shahrukh',
    ]
    return JsonResponse(friends, safe=False)