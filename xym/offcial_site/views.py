from django.shortcuts import render
from django.http.response import JsonResponse

# Create your views here.
def home(request):
    return render(request, "index.html")

def members(request):
    members = [
        {"id": 1, "title": "XYMBaoqing", "price": 89.00},
        {"id": 2, "title": "XYMDsm", "price": 89.00},
        {"id": 3, "title": "XYMPdd", "price": 89.00},
    ]
    return JsonResponse(members, safe=False)