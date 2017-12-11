# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return redirect('/sessionwords')

def session(request):
    return render(request, 'session_words/index.html')

def process(request):
    if request.method == 'POST':
        if len(request.POST['word']) > 0:
            word = {}
            word['word'] = request.POST['word']
            word['color'] = request.POST['color_group']
            word['created_at'] = datetime.now().strftime('%-I:%M:%S%p  %b %d, %Y')
            try:
                word['big'] = request.POST['big']
            except:
                print 'no big'
            try:
                request.session['words']
            except:
                request.session['words'] = []
            templist = request.session['words']
            templist.append(word)
            request.session['words'] = templist
            return redirect('/sessionwords')
        else:
            return redirect('/sessionwords')
    else:
        return redirect('/sessionwords')

def reset(request):
    del request.session['words']
    return redirect('/sessionwords')