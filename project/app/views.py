from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import pandas as pd
import import_ipynb

from django.views.decorators.cache import cache_control, never_cache
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm


# @cache_control(must_revalidate=True)
#@login_required(login_url='/accounts/login/')
def index(request):

    return render(request, 'app/index.html')