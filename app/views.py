from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from .util import UtilOperations


def home(request):
	util_op = UtilOperations()
	if request.method == "POST":
		sqft = float(request.POST.get("Squareft"))
		bhk = request.POST.get("uiBHK")
		bath = request.POST.get("uiBathrooms")
		location = request.POST.get("location")

		result = abs(util_op.get_estimated_price(location, sqft, bhk, bath))

		context = {'result':result}
		return render(request, "app/result.html",context)

	return render(request, "app/app.html")













