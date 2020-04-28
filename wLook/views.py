from django.shortcuts import render

# Create your views here.
# API for this app is coming from https://docs.airnowapi.org/CurrentObservationsByZip/query


def format_page(api):
    if api[0]['Category']['Name'] == "Good":
        category_description = "Ozone in Air is Good"
        category_color = "good"
    elif api[0]['Category']['Name'] == "Moderate":
        category_description = "Ozone in Air is Moderate"
        category_color = "moderate"
    elif api[0]['Category']['Name'] == "Unhealthy for Specific Group":
        category_description = "Ozone in Air is Unhealthy for Specific Group"
        category_color = "usg"
    elif api[0]['Category']['Name'] == "Unhealthy":
        category_description = "Ozone in Air is Unhealth"
        category_color = "unhealthy"
    elif api[0]['Category']['Name'] == "Very Unhealthy":
        category_description = "Ozone in Air is Very Unhealthy"
        category_color = "veryunhealth"
    elif api[0]['Category']['Name'] == "Hazardous":
        category_description = "Ozone in Air is Hazardous"
        category_color = "hazardous"
    return (category_description,  category_color)


def home(request):
    import json
    import requests

    if request.method == "POST":
        zipcode = request.POST['zipcode']
        api_request = requests.get(
            "http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+zipcode+"&distance=5&API_KEY=ED3D331E-5A96-41AE-A8C0-E927A3D7FEFE")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error in api"
    else:
        api_request = requests.get(
            "http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=ED3D331E-5A96-41AE-A8C0-E927A3D7FEFE")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error in api"

    category_description, category_color = format_page(api)
    return render(request, 'home.html', {
        'api': api,
        'category_description': category_description,
        'category_color': category_color})


def about(request):
    return render(request, 'about.html', {})
