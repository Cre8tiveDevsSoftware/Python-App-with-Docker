from django.http import HttpResponse


def splashpage_view(request):
    return HttpResponse("Congratulations!")
