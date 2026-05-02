from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect  # ✅ ADD THIS

urlpatterns = [
    path('admin/', admin.site.urls),

    # apps
    path('account/', include('account.urls')),
    path('events/', include('createevent.urls')),

    path('', lambda request: redirect('loginUser')),
]