from django.http import HttpResponse

HTMLSTRING = """<h1>Congratulations!</h1>"""

def splashpage_view(request):
    # import pdb; pdb.set_trace()
    return HttpResponse(HTMLSTRING)
