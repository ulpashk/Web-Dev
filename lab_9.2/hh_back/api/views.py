from django.shortcuts import render
import json
from django.http.response import JsonResponse
from .models import Company, Vacancy
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@csrf_exempt
def companies(request):
    if request.method == 'GET':
        companiess = Company.objects.all()
        companies_json = [company.to_json() for company in companiess]
        return JsonResponse(companies_json, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        comp = Company.objects.create(name=data['name'], description=data['description'],
                                      city=data['city'], address=data['address'])
        return JsonResponse(comp.to_json())


@csrf_exempt
def company_detail(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)

    if request.method == 'GET':
        return JsonResponse(company.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body)
        name = data['name']
        description = data['description']
        city = data['city']
        address = data['address']
        company.name = name
        company.description = description
        company.city = city
        company.address = address
        company.save()
        return JsonResponse(company.to_json())
    elif request.method == 'DELETE':
        company.delete()
        return JsonResponse({}, status=204)


def vacancies(request):
    vacanciess = Vacancy.objects.all()
    vacancies_json = [vacancy.to_json() for vacancy in vacanciess]
    return JsonResponse(vacancies_json, safe=False)


def vacancy_detail(request, id):
    try:
        vacancy = Vacancy.objects.get(id=id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse(vacancy.to_json(), safe=False)


def company_vacancy(request, id):
    try:
        company = Company.objects.get(id=id)
        vacanciess = Vacancy.objects.filter(company=company)
        vacancies_json = [vacancy.to_json() for vacancy in vacanciess]
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse(vacancies_json, safe=False)


def vacancy_company(request, id):
    try:
        vacancyy = Vacancy.objects.get(id=id)
        companiess = Company.objects.filter(vacancy=vacancyy)
        companies_json = [company.to_json() for company in companiess]
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse(companies_json, safe=False)

def top10_vacancies(request):
    vacanciess = Vacancy.objects.all().order_by('-salary')[:10]
    vacancies_json = [vacancy.to_json() for vacancy in vacanciess]
    return JsonResponse(vacancies_json, safe=False)
