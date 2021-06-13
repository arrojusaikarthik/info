from credentials.models import allorderslist, logos, ongoingridesnow, alertsandnote
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from datetime import datetime

# Create your views here.


def home(request):
    logoshere = logos.objects.all()
    alerts = alertsandnote.objects.all()
    fests = ongoingridesnow.objects.all()
    return render(request, 'reglog.html', {'logoshere': logoshere, 'fests': fests, 'alerts': alerts})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'details.html')

        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request, 'User created')
                return redirect('login')

        else:
            messages.info(request, 'Password not matching')
            return redirect('register')
            return redirect('/')

    else:
        return render(request, 'register.html')


def logout(request):
    logoshere = logos.objects.all()
    alerts = alertsandnote.objects.all()
    fests = ongoingridesnow.objects.all()
    auth.logout(request)

    return render(request, 'reglog.html', {'logoshere': logoshere, 'fests': fests, 'alerts': alerts})


def best(request):
    logoshere = logos.objects.all()
    ridername = str(request.POST['name'])
    orderid = request.POST['order1']
    ridedate = request.POST['date1']
    distance_in_km = 5
    time_in_minutes = 0.2
    s1 = float(request.POST['reading1'])
    s2 = float(request.POST['reading2'])
    distance_result = s2-s1
    s3 = request.POST['time1']
    s4 = request.POST['time2']
    format = '%H:%M'
    time = datetime.strptime(s4, format) - datetime.strptime(s3, format)
    time_result = time.total_seconds()/60
    result = distance_result*distance_in_km+time_result*time_in_minutes
    promo_code = str(request.POST["promocode"])
    if promo_code == "SAI123":
        dis_amount = result - (result * 6) / 100
        diss_amount = 'Promocode Applied,'

    elif promo_code == "SK123":
        dis_amount = result - (result * 6) / 100
        diss_amount = 'Promocode Applied,'

    else:
        dis_amount = result
        diss_amount = "Invalid Promocode,"
    return render(request, 'finaldetails.html', {'logoshere': logoshere, 'rdate': ridedate, 'rname': ridername, 'oid': orderid, 'da1': diss_amount, 'promo': promo_code, 'reading1': s1, 'reading2': s2, 'time1': s3, 'time2': s4, 'timeres': time_result, 'res': distance_result,  'da': dis_amount, 'total': result})


def orderid(request):
    logoshere = logos.objects.all()
    allordershere = allorderslist.objects.all()
    return render(request, 'allorders.html', {'allordershere': allordershere, 'logoshere': logoshere})
