from django.shortcuts import render, redirect
import random
from time import gmtime, strftime

def index(request):
  try:
    request.session['gold']
    request.session['activity']
  except:
    request.session['gold'] = 0
    request.session['activity'] = []

  return render(request, 'gold/index.html')

def process_gold(request):
  local = request.POST['local']
  time = strftime("(%Y/%m/%d %I:%M %p)")
  if (local == 'farm'):
    gold = random.randrange(10,21)
  elif (local == 'cave'):
    gold = random.randrange(5,11)
  elif (local == 'house'):
    gold = random.randrange(2,6)
  elif (local == 'casino'):
    gold = random.randrange(-50,51)
  else:
    gold = -51
    request.session['gold'] = 0

  request.session['gold'] += gold
  if (gold >= 0):
    result = 'win'
    activity = "Earned " + str(gold) + " gold from the " + local + "! " + time
  elif (gold == -51):
    result = 'lose'
    activity = "You lost your way and got mugged. Lost all your gold!" + time
  else:
    result = 'lose'
    activity = "Entered a casino and lost " + str(gold) + " gold.  Lesson learned? " + time
  trip = result, activity
  request.session['activity'].insert(0, trip)
  return redirect('index')

def reset(request):
  request.session.pop('gold')
  request.session.pop('activity')
  return redirect('index')
