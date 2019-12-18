# django
from django.http import HttpResponse
from django.http import JsonResponse

# utilities
from datetime import datetime

""" En este archivo están las vistas de nuestra app"""
def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Current server time is: {}'.format(now))

def sort_numbers(request):
    numbers = request.GET['numbers']
    numbers = numbers.split(',')
    numbers = list(map(int, numbers))
    numbers.sort()
    sorted_numbers = {}

    for index, number in enumerate(numbers):
        dict_index = 'number_{}'.format(index+1)
        sorted_numbers[dict_index] = number

    response = {
        'status': 'Ok',
        'numbers': sorted_numbers,
        'message': 'Numbers sorted successfully'
    }
    return JsonResponse(response)

def say_hi(request, name, age):
    if age < 12:
        message = 'Sorry {} you are not allowed here'.format(name)
    else:
        message = 'Hi {}, welcome to Platzigram!'.format(name)
    return HttpResponse(message)


