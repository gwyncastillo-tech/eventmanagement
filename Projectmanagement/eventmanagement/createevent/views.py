from django.views import View
from django.shortcuts import render, redirect
from .models import Emergency
from account.models import Account


class CreateEmergency(View):
    template_name = 'create_emergency.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.session.get('username')

        if not username:
            return redirect('loginUser')

        try:
            user = Account.objects.get(username=username)
        except Account.DoesNotExist:
            return redirect('loginUser')

        title = request.POST.get('title')
        description = request.POST.get('description')

        if not title or not description:
            return redirect('createEmergency')

        Emergency.objects.create(
            user=user,
            title=title,
            description=description,
            status="Pending"
        )

        return redirect('loginUser')


class ResponderDashboard(View):
    template_name = 'responder.html'

    def get(self, request):
        emergencies = Emergency.objects.all().order_by('-emergencyID')

        return render(request, self.template_name, {
            'emergencies': emergencies
        })

    def post(self, request):
        emergency_id = request.POST.get('id')
        action = request.POST.get('action')

        username = request.session.get('username')

        try:
            responder = Account.objects.get(username=username)
            emergency = Emergency.objects.get(emergencyID=emergency_id)

            if action == "dispatch":
                emergency.status = "Dispatched"

            elif action == "complete":
                emergency.status = "Completed"
                emergency.handled_by = responder  # ✅ SAVE WHO HANDLED IT

            emergency.save()

        except Emergency.DoesNotExist:
            pass
        except Account.DoesNotExist:
            pass

        return redirect('responderDashboard')