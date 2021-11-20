from django.shortcuts import render
from django.views.generic import TemplateView
from survey.forms import SelectPatient
import requests

# Create your views here.


def get_name(request):
    if request.method == 'POST':
        form = SelectPatient(request.POST)
        if form.is_valid():
            tcid = form.cleaned_data['tcid']
            dosya_no = form.cleaned_data['dosya_no']
            url = f"https://dummy.restapiexample.com/api/v1/employee/{tcid}"
            response = requests.Request(url)
            if response.status_code == "200":
                data = response.json()
                print(data)
                return data 
