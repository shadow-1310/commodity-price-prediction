from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import numpy as np
import pickle

car = pd.read_csv("car/notebooks/data/clean_car.csv")
model=pickle.load(open('car/notebooks/data/model_svr.pkl','rb'))

def index(request):
    companies=sorted(car['company'].unique())
    car_models=sorted(car['name'].unique())
    years=sorted(car['year'].unique(),reverse=True)
    fuel_types=car['fuel'].unique()
    owner = car['owner'].unique()
    sellers = car['seller_type'].unique() 
    transmission = car['transmission'].unique()

    params = {'companies':companies,
              'car_models':car_models,
              'years':years,
              'fuel_types':fuel_types,
              'owners':owner,
              'sellers':sellers,
              'transmission':transmission
              }
    
    return render(request, 'car/index.html', params)

def predict(request):
    
    company= request.POST.get('company')
    car_model= request.POST.get('car_models')
    year= request.POST.get('year')
    fuel_type= request.POST.get('fuel_type')
    driven= request.POST.get('kilo_driven')
    seller = request.POST.get('seller')
    trans = request.POST.get('trans')
    owner = request.POST.get('owner')

    prediction=np.exp(model.predict(pd.DataFrame(columns=['year', 'km_driven', 'fuel', 'seller_type', 'transmission', 'owner', 'company', 'model'],data=np.array([year, driven, fuel_type, seller, trans, owner, company, car_model]).reshape(1, 8))))
    print(prediction)

    return HttpResponse(str(np.round(prediction[0], 2)))

# Create your views here.
