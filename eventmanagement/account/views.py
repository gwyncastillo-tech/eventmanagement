from django.shortcuts import render
from django.views import View
from .form import StudentForm
from .models import Account


class HomeView(View):
    template_name = 'index.html'

    def get(self, request):
        strName = 'Jose'
        return render(request, self.template_name, {'strname': strName})


class RegisterStudent(View):
    template_name = 'addNewStudentt.html'

    def get(self, request):
        form = StudentForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()

            Account.objects.create(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                firstname=form.cleaned_data['firstname'],
                lastname=form.cleaned_data['lastname'],
                type='S'
            )

            return render(request, self.template_name, {
                'form': StudentForm(),
                'success': 'Student registered successfully!'
            })

        else:
            print(form.errors)
            return render(request, self.template_name, {'form': form})

class LoginUser(View):
            template_name = 'login.html'

            def get(self, request):
                return render(request, self.template_name)

            def post(self, request):
                username = request.POST.get('username')
                password = request.POST.get('password')

                try:
                    user = Account.objects.get(
                        username=username,
                        password=password
                    )

                    return render(request, self.template_name, {
                        'success': f'Welcome {user.firstname}!'
                    })

                except Account.DoesNotExist:
                    return render(request, self.template_name, {
                        'error': 'Invalid username or password'
                    })