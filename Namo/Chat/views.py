from django.shortcuts import render

def chat(req):
    return render(req, 'Chat/chat.html')