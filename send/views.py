from django.shortcuts import render

# Create your views here.
from time import sleep
from os import system , name
from concurrent.futures import ThreadPoolExecutor
from inspect import getmembers, isfunction
from send.Api import sms, call
from django.http import HttpResponse

SMS_SERVICES = list(i[0] for i in getmembers(sms, isfunction))
CALL_SERVICES = list(i[0] for i in getmembers(call, isfunction))

def send_sms(request,a,y):
    x = a
    phone = y
    with ThreadPoolExecutor(max_workers=20) as executor:
        for j in range(x):
            for k in range(len(SMS_SERVICES)):
                executor.submit(getattr(sms, SMS_SERVICES[k]), phone)
            if (j != 0) and (j % 5) == 0:
                executor.submit(getattr(call, CALL_SERVICES[x]), phone)
                x += 1
                if x > len(CALL_SERVICES) - 1:
                    x = 0
            print(f"Round {j+1} Completed Gg")
            sleep(0.2)
    print("Finish")
    return render (request,'html.html')


