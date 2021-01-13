"""Platzigram views"""

# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime

import json

def hello_world(request):
    """Return greeting"""
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')

    return HttpResponse('Ohhh hi! Current server time is {now}'.format(now=now))


def hi(request):
    """Hi"""
    # import pdb; pdb.set_trace()
    numbers = '{' + request.GET['numbers'] + '}'
    
    y = json.dumps(numbers)
    a = 2
    print(type(numbers))
    print(json.loads(numbers))

    #numbers.sort()
    return HttpResponse(numbers)