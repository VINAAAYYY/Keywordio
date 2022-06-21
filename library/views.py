from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .forms import bookForm
import json
from rest_framework.permissions import IsAuthenticated, AllowAny
# Create your views here.

class homepage(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        bookId = request.query_params.get('id')
        data = Books.objects.all().values()
        admin = False
        if request.user.is_authenticated:
            admin=True
        if bookId:
            if not admin:
                return redirect("homepage")
            obj = Books.objects.get(id=bookId)
            form = bookForm(instance=obj)
            context = {'form' : form, 'm':True, 'id':bookId}
            return render(request, 'form.html', context)
        return render(request, 'homepage.html', {"data":data, "admin":admin})
    
    def post(self, request):
        try:
            bookId = int(request.POST['id'])
        except:
            bookId=None
        try:
            method = request.POST['m']
        except:
            method=None
            
        if(method=="del"):
            obj = Books.objects.get(id=bookId)
            obj.delete()

        else:
            form = bookForm(request.POST)
            if(bookId):
                obj = Books.objects.get(id=bookId)
                form = bookForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
        return redirect("homepage")

def addBook(request):
    permission_classes = [IsAuthenticated]
    form = bookForm()
    context = {'form' : form, 'm':False}
    return render(request, 'form.html', context)