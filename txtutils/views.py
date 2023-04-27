# created file

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    # return HttpResponse(''' Home 
    # <br>
    # <a type="button" href = "http://127.0.0.1:8000/removepunc"> 
    # Remove Punctuator</a>
    # <br>
    # <a type="button" href = "http://127.0.0.1:8000/capitalizeFirst"> Capitalization</a>
    # <br>
    # <a type="button" href = "http://127.0.0.1:8000/newlineremove"> New Line Remove</a>
    # <br>
    # <a type="button" href = "http://127.0.0.1:8000/spaceremover"> Space Remover</a>
    # <br>
    # <a type="button" href = "http://127.0.0.1:8000/charcount"> Character Count</a>

    # ''')
# def chatgpt(request):
#     return HttpResponse('''<a href = "https://chat.openai.com/chat">ChatGpt</a>''')
# def news(request):
#     return HttpResponse('''<a href="https://news.google.com/">GoogleNews</a>''')S
# def about(request):
#     return HttpResponse("Great")


# def removepunc(request):
#     # getting text from home textarea
#     djtext = request.GET.get('text', 'default')
#     print(djtext)
#     # analyze the text
#     return HttpResponse('''Remove Punctuator
#     <br>
#     <a href = "http://127.0.0.1:8000/">Home</a>
#     ''')
# def capfirst(request):
#     return HttpResponse('''Capitalization
#     <br>
#     <a href = "http://127.0.0.1:8000/">Home</a>
#     ''')
# def newlineremove(request):
#     return HttpResponse('''New Line Remove
#     <br>
#     <a href = "http://127.0.0.1:8000/">Home</a>
#     ''')
# def spaceremover(request):
#     return HttpResponse('''Space Remover
#     <br>
#     <a href = "http://127.0.0.1:8000/">Home</a>
#     ''')
# def charcount(request):
#     return HttpResponse('''Character Count
#     <br>
#     <a href = "http://127.0.0.1:8000/">Home</a>
#     ''')



def analyze(request):
    # getting text from home textarea
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', "off")
    fullcaps =  request.GET.get('fullcaps', "off")
    newlineremove = request.GET.get('newlineremove', "off") 
    spaceremover = request.GET.get('spaceremover', "off")
    charcount = request.GET.get('charcount', "off")
    extraspaceremover = request.GET.get('extraspaceremover', "off")
    
    print(removepunc)
    print(djtext)
    
    if removepunc == "on":
        # analyzed = djtext
        punctuations = ''' !@#$%^&*()[]}{:;?/\'"~`_-<>.,'''
        analyzed = ""               
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        jnm = {'purpose':'Removed punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # analyze the text
        # return render(request, 'analyze.html', jnm)
    
    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        
        jnm = {'purpose':'Changed to Upper Case', 'analyzed_text': analyzed}
        djtext = analyzed
        # analyze the text
        return render(request, 'analyze.html', jnm)
    
    if(newlineremove == "on"):
        analyzed= ""
        for char in djtext:
            if char != "\n" and char !="\r":
                analyzed = analyzed + char
            else:
                print("no")
        jnm = {'purpose':'New line removed', 'analyzed_text': analyzed}
        # analyze the text
        djtext = analyzed
        # return render(request, 'analyze.html', jnm)
    
    if(spaceremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != " ":
                analyzed = analyzed+char
        jnm = {'purpose':'Spaced removed', 'analyzed_text': analyzed}
        # analyze the text
        djtext = analyzed
        # return render(request, 'analyze.html', jnm)
    
    if(charcount == "on"):
        analyzed = len(djtext)
        jnm = {'purpose':'Character Counted', 'analyzed_text': analyzed}
        # analyze the text
        djtext = analyzed
        return render(request, 'analyze.html', jnm)     

    if(extraspaceremover == "on"):
        analyzed = ""
        for i , char in enumerate(djtext):
            if djtext[i] == " " and djtext[i+1] == " ":
                pass
            else:
                analyzed = analyzed+char
        jnm = {'purpose':'Character Counted', 'analyzed_text': analyzed}
        # analyze the text
        djtext = analyzed
        # return render(request, 'analyze.html', jnm)    

    # else:
    #     return HttpResponse("Error")
     
    if(removepunc!="on" and  extraspaceremover!="on" and charcount!="on" and spaceremover!= "on" and newlineremove!= "on" and removepunc != "on" and fullcaps!= "on"):
        return HttpResponse("Error - Please select ont the fields mentioned on the last page, Thank you!")
        

    return render(request, 'analyze.html', jnm)    

    # return HttpResponse('''Remove Punctuator
    # <br>
    # <a href = "http://127.0.0.1:8000/">Home</a>
    # ''')
