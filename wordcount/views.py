from django.shortcuts import render
import operator
def home(request):
    return render(request,'wordcount/home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    word_dict = {}
    for word in wordlist:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    sorted_words = sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)  #convert the dictionary to a list

    return render(request,'wordcount/count.html', {'fulltextkey': fulltext,
                                                    'wordcountkey': len(wordlist),
                                                    'sorted_words' : sorted_words})


def about(request):
    return render(request,'wordcount/about.html')                                                