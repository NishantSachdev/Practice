from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    '''
    return HttpResponse("<h1>Homepage</h1> <hr> <a href='/capfirst'>Capitalize first letter</a> <hr> <a href='/remspace'>Remove spaces from text</a> <hr> <a href='/add2nos'>Add 2 numbers</a> <hr> <a href='/openfile'>Open text files</a>")
    '''
    

def analyze(request):
    #Get the text
    djtext = request.GET.get('text', 'default')

    # Check checkbox values
    removepunc = request.GET.get('removepunc', 'off')
    capfirst = request.GET.get('capfirst', 'off')
    remspace = request.GET.get('remspace', 'off')
    upper = request.GET.get('upper', 'off')
    lower = request.GET.get('lower', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        djtext=analyzed
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)

    if capfirst=="on":
        list1=[]
        list1=djtext.split(" ")
        analyzed=""
        for x in list1:
            analyzed=analyzed+x.capitalize()+" "
        djtext=analyzed
        params={"purpose":"Capitalized first letter","analyzed_text":analyzed}
        # return render(request,"analyze.html",params)

    if remspace=="on":
        analyzed=""
        for char in djtext:
            if char !=" ":
                analyzed=analyzed+char
        djtext=analyzed
        params={"purpose":"Removed Spaces", "analyzed_text":analyzed}
        #return render(request,"analyze.html",params)

    if upper=="on":
        analyzed=djtext.upper()
        djtext=analyzed
        params={"purpose":"UPPERCASE","analyzed_text":analyzed}
        #return render(request,"analyze.html",params)

    if lower=="on":
        analyzed=djtext.lower()
        djtext=analyzed
        params={"purpose":"lowercase","analyzed_text":analyzed}
        #return render(request,"analyze.html",params)

    return render(request, "analyze.html", params)

    
    
