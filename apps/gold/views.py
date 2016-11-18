from django.shortcuts import render, redirect
import random
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'gold/index.html')

def process(request):
    try:
        request.session['gold']
    except KeyError:
        request.session['gold'] = 0
    try:
        request.session['activities']
    except KeyError:
        request.session['activities'] = []
    if request.POST['building'] == 'farm':
        gold = random.randrange(10,21)
    elif request.POST['building'] == 'cave':
        gold = random.randrange(5, 11)
    elif request.POST['building'] == 'house':
        gold = random.randrange(2, 6)
    elif request.POST['building'] == 'casino':
        gold = random.randrange(-50, 51)

    activity = ''
    time = datetime.now().strftime('%Y/%m/%d %I:%M %p')
    if gold >=0:
        activity += 'Earned ' + str(gold) + ' golds from the ' + str(request.POST['building'])
    else:
        activity += 'Entered a casino and lost ' + str(gold) + ' golds... Ouch...'

    activity += '! (' + str(time) + ')'
    request.session['gold'] += gold
    request.session['activities'].insert(0, activity)
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')
