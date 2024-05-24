from django.shortcuts import render, redirect, get_list_or_404

from web.forms import ContactForm
from web.models import *

from django.contrib.auth.views import LoginView, logout_then_login
from django.contrib.auth.decorators import login_required

import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    inmuebles = Inmueble.objects.all()
    return render(request, 'index.html', {'inmuebles': inmuebles})


