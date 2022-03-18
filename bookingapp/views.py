
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django import forms
from .models import Guest, GManager, Apartment, AppName, AppStatus, Payment, PaymentType
