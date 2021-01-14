"""Platzigram views"""

# Django
from django.http import HttpResponse
#from django.http import JsonResponse

# Utilities
from datetime import datetime
import json



def hello_world(request):
    """Return greeting"""
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')

    return HttpResponse('Ohhh hi! Current server time is {now}'.format(now=now))


def sort_integer(request):
    """Return a JSON response with sorted integer"""
    # import pdb; pdb.set_trace()
    numbers = request.GET['numbers']
    mList = [int(e) if e.isdigit() else e for e in numbers.split(',')]
    mList.sort()
    data = {
        'status': 'ok',
        'numbers': mList,
        'message': 'Integers sorted successfully'
    }
    #numberList = JsonResponse({ "numbers" : mList},json_dumps_params={'indent': 4})

    print(data)

    return HttpResponse(json.dumps(data), content_type='application/json')


def say_hi(request, name, age):
    """Return a greeting. """
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello, {}! welcome to platzigram'.format(name)
    
    return HttpResponse(message)
