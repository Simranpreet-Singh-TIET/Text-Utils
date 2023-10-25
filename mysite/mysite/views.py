from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index2.html')

def removepunc(djtext):
    punc='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    analyzed_text=""
    for char in djtext:
        if char not in punc:
            analyzed_text=analyzed_text+char
    return analyzed_text
def capitalise(djtext):
    return djtext.upper()
def newlineremove(djtext):
    return ''.join(djtext.splitlines())
def spaceremovefunc(djtext):
    return ' '.join(djtext.split())
def charcount(djtext):
    return len(djtext.replace(" ",""))




def analyse(request):


    djtext = request.GET.get("text","default")
    djremovepunc=request.GET.get("removepunc","off")
    djcapitalise=request.GET.get("capitalise","off")
    djnewlineremove=request.GET.get("newlineremove","off")
    djspaceremove=request.GET.get("spaceremove","off")
    djcharccount=request.GET.get("charcount","off")
    analyzed_text=djtext


    func=""
    if(djremovepunc=="on"):
        analyzed_text=removepunc(analyzed_text)
        func=func+"   Removed Punctuation "
    if(djcapitalise=="on"):
        analyzed_text=capitalise(analyzed_text)
        func=func+"  Capitalised "
    if(djnewlineremove=="on"):
        func=func+"  New lines Removed "
        analyzed_text=newlineremove(analyzed_text)
        # func=func+" New lines Removed "
    if(djspaceremove=="on"):
        analyzed_text=spaceremovefunc(analyzed_text)
        func=func+"  Removed Spaces "
    if(djcharccount=="on"):
        func=func +"  Counted Character "
        analyzed_text=analyzed_text+"\nCharacter Count: " + str(charcount(analyzed_text))
    params ={"func":func,"text":analyzed_text}
    return render(request,"analysed.html",params)









