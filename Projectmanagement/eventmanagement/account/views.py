from django.shortcuts import render, redirect
from django.views import View
from .models import Account
from datetime import datetime
from createevent.models import Emergency


class HomeView(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)


class RegisterUser(View):
    template_name = 'register.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        dob_input = request.POST.get('dob')

        dob = None
        if dob_input:
            try:
                dob = datetime.strptime(dob_input, "%m/%d/%Y").date()
            except ValueError:
                dob = None

        Account.objects.create(
            username=request.POST.get('username'),
            password=request.POST.get('password'),
            fullname=request.POST.get('fullName'),
            email=request.POST.get('email'),
            dob=dob,
            address=request.POST.get('address'),
            phone=request.POST.get('phone'),
            type=int(request.POST.get('type'))
        )

        request.session.flush()
        return redirect('loginUser')


class LoginUser(View):
    template_name = 'login.html'

    def get(self, request):
        username = request.session.get('username')

        if username:
            try:
                user = Account.objects.get(username=username)
                return render(request, self.template_name, {
                    'success': user.fullname,
                    'type': user.type
                })
            except Account.DoesNotExist:
                pass

        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = Account.objects.get(
                username=username,
                password=password
            )

            request.session['username'] = user.username

            return redirect('loginUser')

        except Account.DoesNotExist:
            return render(request, self.template_name, {
                'error': 'Invalid username or password'
            })


class EditProfile(View):
    template_name = 'editProfile.html'

    def get(self, request):
        username = request.session.get('username')

        if not username:
            return redirect('loginUser')

        user = Account.objects.get(username=username)

        return render(request, self.template_name, {
            'user': user
        })

    def post(self, request):
        username = request.session.get('username')

        if not username:
            return redirect('loginUser')

        user = Account.objects.get(username=username)

        user.fullname = request.POST.get('fullName')
        user.email = request.POST.get('email')
        user.address = request.POST.get('address')
        user.phone = request.POST.get('phone')

        dob_input = request.POST.get('dob')
        if dob_input:
            try:
                user.dob = datetime.strptime(dob_input, "%m/%d/%Y").date()
            except ValueError:
                pass

        user.save()

        return redirect('loginUser')


class LogoutUser(View):
    def get(self, request):
        request.session.flush()
        return redirect('loginUser')


class MyEmergencies(View):
    def get(self, request):
        username = request.session.get('username')

        if not username:
            return redirect('loginUser')

        user = Account.objects.get(username=username)

        emergencies = Emergency.objects.filter(user=user).order_by('-emergencyID')

        return render(request, 'my_emergencies.html', {
            'emergencies': emergencies
        })