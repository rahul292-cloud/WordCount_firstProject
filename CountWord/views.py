from django.http import HttpResponse
from django.shortcuts import render
#import opertor
def Home(request):
    return render(request, 'home.html' )

def about(request):
    return render(request, 'about.html' )

def count(request):
    fulltext = request.GET['fulltext']
    worldlist = fulltext.split()
    word_dict = {}
    
    for word in worldlist:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

   # sort_word = sorted(word_dict.items(), key=operator.itemgetter(1), reverse = True)
    
    return render(request, 'count.html', {'fulltext':fulltext , 'count':len(worldlist) , 'word_dict':word_dict.items()})
