from django.http import HttpResponse, JsonResponse
#take Request from Urls and return a response to the user
def home_page(request):
    print("Home page accessed")
    return HttpResponse("Welcome to the Company API!")

def company_list(request):
    print("Company list accessed")
    data=[
        {"Name": "Sohel",
          "Age": 24,
          "City": "Dhaka"
        }
    ]
    return JsonResponse(data, safe=False)