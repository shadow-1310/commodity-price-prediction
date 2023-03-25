from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import numpy as np
import pickle

laptop = pd.read_csv("laptop/notebooks/data/clean_laptop.csv")
pipe = pickle.load(open('laptop/notebooks/data/pipe.pkl','rb'))


def index(request):
    companies = sorted(laptop['Company'].unique())
    types = sorted(laptop['TypeName'].unique())
    ram = sorted(laptop['Ram'].unique())
    gpu = sorted(laptop['Gpu'].unique())
    cpu = sorted(laptop['Cpu_brand'].unique())
    hdd = sorted(laptop['HDD'].unique())
    ssd = sorted(laptop['SSD'].unique())
    os = sorted(laptop['os'].unique())
    params = {'companies': companies,
              'types':types,
              'ram':ram,
              'gpu':gpu,
              'cpu':cpu,
              'hdd':hdd,
              'ssd':ssd,
              'os':os,
              }
    return render(request, 'laptop/index.html', params)

def predict(request):
    company= request.POST.get('company')
    type= request.POST.get('type')
    ram= request.POST.get('ram')
    cpu= request.POST.get('cpu')
    gpu= request.POST.get('gpu')
    touchscreen= request.POST.get('touchscreen')
    ips= request.POST.get('ips')
    weight= request.POST.get('weight')
    ppi= request.POST.get('ppi')
    hdd= request.POST.get('hdd')
    ssd= request.POST.get('ssd')
    os= request.POST.get('os')

    prediction = np.exp(pipe.predict(pd.DataFrame(columns=['Company', 'TypeName', 'Ram', 'Gpu', 'Weight', 'Touchscreen', 'ips', 'ppi', 'Cpu_brand', 'HDD', 'SSD', 'os'],data=np.array([company, type, ram, gpu, weight, touchscreen, ips, ppi, cpu, hdd, ssd, os]).reshape(1, 12))))
    print(prediction)
    return HttpResponse(str(np.round(prediction[0], 2)))

