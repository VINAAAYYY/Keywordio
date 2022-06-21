from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CustomUser as User
from rest_framework.authtoken.models import Token

class signUp(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        data = request.data
        if not User.objects.filter(username=data['email']).exists():
            user = User.objects.create(
                username=data['email'], email=data['email'], first_name=data['first_name'], last_name=data['last_name'])
            user.set_password(data['password'])
            user.save()

            request.META.get('HTTP_AUTHORIZATION')
            Token.objects.create(user=user)
            login(request, user)
            return redirect('signin')

        else:
            return render(request, 'signup.html', {"exception": "Email Address Already Present"})
    
# permission classes will be forever allowany
class signIn(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        user = request.user
        if user.is_authenticated:
            return redirect('homepage')
        return render(request, 'login.html')

    def post(self, request):
        data = request.data
        if User.objects.filter(username=data['email'] ,email=data['email']).exists():
            request.META.get('HTTP_AUTHORIZATION')

            user = User.objects.filter(username=data['email']).first()
            matchcheck = authenticate(
                username=data["email"], password=data["password"])

            if matchcheck:
                login(request, user)
                return redirect('homepage')
            return render(request, 'login.html', {"exception": "Password Not Matched"})

        else:
            return render(request, 'login.html', {"exception": "Email Address NOT Present"})
            


class signOut(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        logout(request)
        return redirect("signin")


class changePassword(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return render(request, 'pwdch.html')

    def post(self, request):
        user = request.user
        data = request.data
        if data["password1"] != data["password2"]:
            return render(request, 'pwdch.html', {"exception": "Passwords Donot Match"})
        matchcheck = authenticate(
            username=user.username, password=data["currPass"])
        if matchcheck:
            user.set_password(data["password1"])
            user.save()
            login(request, user)
            return redirect('signin')
        return render(request, 'pwdch.html', {"exception": "Enter Correct Password"})
