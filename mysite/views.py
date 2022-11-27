
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyse(request):
    djtext = request.POST.get("text","default")
    removepunc = request.POST.get("removepunc","off")
    fullcaps = request.POST.get("fullcaps","off")
    newlineremover = request.POST.get("newlineremover","off")
    extraspaceremover = request.POST.get("extraspaceremover","off")

    if (removepunc == "on"):
        punctuations = '''!()_[]{};:'"\,<>./?@#$%^&*-~'''
        analysed = ""
        for char in djtext:
            if char not in punctuations:
                analysed = analysed + char

        params = {"purpose":"Remove Punctuations", "analysed_text":analysed}
        djtext = analysed
        #return render(request, "analyse.html", params)


    if (fullcaps=="on"):
        analysed=""
        for char in djtext:
            analysed = analysed+ char.upper()
        
        params = {"purpose":"Changed to Uppercase", "analysed_text":analysed}
        djtext = analysed
        #return render(request, "analyse.html", params)


    if (newlineremover == "on"):
        analysed=""
        for char in djtext:
            if char !="\n" and char!="\r":
                analysed = analysed + char
        
        params = {"purpose":"Removed New lines", "analysed_text":analysed}
        djtext = analysed
        #return render(request, "analyse.html", params)

    
    if (extraspaceremover == "on"):
        analysed=""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analysed = analysed + char
        
        params = {"purpose":"Spaces removed", "analysed_text":analysed}

    if(removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on"):
        return HttpResponse("Error")
    
    return render(request, "analyse.html", params)