from django.shortcuts import render, redirect
from .models import Company
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect
import json
import requests

# Create your views here.
# https://www.freecodecamp.org/news/how-to-create-auto-updating-data-visualizations-in-python-with-matplotlib-and-aws/ 
def stocks(request):
    if request.method == "POST":
        stockcode = request.POST['stockcode']
        api_request = requests.get(
            "https://cloud.iexapis.com/stable/stock/MSFT/quote?token=pk_17a8c4d6ed224f01baa963bb2472e7ff")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error in api"
    else:
        api_request = requests.get(
            "https://cloud.iexapis.com/stable/stock/MSFT/quote?token=pk_17a8c4d6ed224f01baa963bb2472e7ff")
        # "https://cloud.iexapis.com/stable/stock/"+stockcode+"/quote?token=pk_17a8c4d6ed224f01baa963bb2472e7ff")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error in api"
    return render(request, 'stocks.html', {'api': api})

def portfolio(request):
    if request.method == 'POST':
        ticker = request.POST['ticker']
        api_request = requests.get(
            "https://cloud.iexapis.com/stable/stock/"+ticker+"/quote?token=pk_17a8c4d6ed224f01baa963bb2472e7ff")
        try:
            api = json.loads(api_request.content)
            new_entry = Company()
            new_entry.ticker=api['symbol']
            new_entry.co_name=api['companyName']
            new_entry.latest_price=api['latestPrice']
            new_entry.previous_price=api['previousClose']
            new_entry.pe_ratio=api['peRatio']
            new_entry.marketcap=api['marketCap']
            new_entry.change=api['ytdChange']
            new_entry.save()
            all_companies = Company.objects.all
            messages.success(request, ('In TRY Loop!!'))
            return render(request, 'portfolio.html', {'all_companies': all_companies})
        except Exception as e:
            api = "Error in api"
            all_companies = Company.objects.all
            messages.success(request, ('ERROR!!'))
            return render(request, 'portfolio.html', {'all_companies': all_companies})

    else:
        all_companies = Company.objects.all
        return render(request, 'portfolio.html', {'all_companies': all_companies})


def deletestock(request, id):
    Company.objects.filter(pk=id).delete()
    #item.delete()
    messages.success(request, ('Item deleted from the list!!'))
    return redirect('portfolio')