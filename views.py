from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    if 'words' in request.session:
        context = {
            "words": request.session['words']
        }
        return render(request, 'sessionwords_app/index.html', context)
    return render(request, 'sessionwords_app/index.html')

def add_word(request):
    word  = request.POST['word']
    color = request.POST['color']
    if 'big' in request.POST:
        size = 'big'
    else:
        size = 'normal'
    if 'words' not in request.session:
        request.session['words'] = []

    newWord = {
        'word':  word,
        'color': color,
        'size':  size,
    }

    words = request.session['words']
    words.append(newWord)
    request.session['words'] = words
    for word in request.session['words']:
        print(word)
    return redirect('/session_words')

def clear(request):
    request.session['words'] = []
    return redirect('/session_words')
