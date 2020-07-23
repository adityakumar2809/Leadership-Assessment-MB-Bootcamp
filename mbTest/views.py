from django.shortcuts import render
from django.http import HttpResponse

import math

from . import models

# Create your views here.


def mb_test_view(request):
    return render(request, 'mbTest/test_page.html')


def mb_test_view_ajax(request):
    if request.method == 'POST':
        data_dict = {}
        data_list = []
        mb_response = models.MBResponse()
        response_sum = 0

        data_dict['name'] = request.POST.get('name', None)
        data_list.append(request.POST.get('name', None))
        mb_response.name = request.POST.get('name', None)


        for i in range(1,15):
            value = int(request.POST.get(f'q{i}', None))
            data_dict[f'q{i}'] = value
            data_list.append(value)
            response_grade = 0

            if i==1:
                if value == 1:
                    response_grade = 2
                elif value == 2:
                    response_grade = 2
                elif value == 3:
                    response_grade = 4
                elif value == 4:
                    response_grade = 3
                elif value == 5:
                    response_grade = 3
            elif i==2:
                if value == 1:
                    response_grade = 2
                elif value == 2:
                    response_grade = 4
                elif value == 3:
                    response_grade = 1
                elif value == 4:
                    response_grade = 3
            elif i==3:
                if value == 1:
                    response_grade = 1
                elif value == 2:
                    response_grade = 2
                elif value == 3:
                    response_grade = 4
                elif value == 4:
                    response_grade = 3
            elif i==4:
                if value == 1:
                    response_grade = 3
                elif value == 2:
                    response_grade = 1
                elif value == 3:
                    response_grade = 2
                elif value == 4:
                    response_grade = 4
            elif i==5:
                if value == 1:
                    response_grade = 1
                elif value == 2:
                    response_grade = 3
                elif value == 3:
                    response_grade = 3
                elif value == 4:
                    response_grade = 4
                elif value == 5:
                    response_grade = 2
            elif i==6:
                if value == 1:
                    response_grade = 1
                elif value == 2:
                    response_grade = 3
                elif value == 3:
                    response_grade = 4
                elif value == 4:
                    response_grade = 4
                elif value == 5:
                    response_grade = 2
            elif i==7:
                if value == 1:
                    response_grade = 4
                elif value == 2:
                    response_grade = 3
                elif value == 3:
                    response_grade = 3
                elif value == 4:
                    response_grade = 1
                elif value == 5:
                    response_grade = 3
            elif i==8:
                if value == 1:
                    response_grade = 1
                elif value == 2:
                    response_grade = 2
                elif value == 3:
                    response_grade = 4
                elif value == 4:
                    response_grade = 3
            elif i==9:
                if value == 1:
                    response_grade = 1
                elif value == 2:
                    response_grade = 4
                elif value == 3:
                    response_grade = 3
                elif value == 4:
                    response_grade = 1
                elif value == 5:
                    response_grade = 2
            elif i==10:
                if value == 1:
                    response_grade = 1
                elif value == 2:
                    response_grade = 4
                elif value == 3:
                    response_grade = 3
                elif value == 4:
                    response_grade = 4
                elif value == 5:
                    response_grade = 1
            elif i==11:
                if value == 1:
                    response_grade = 1
                elif value == 2:
                    response_grade = 3
                elif value == 3:
                    response_grade = 4
                elif value == 4:
                    response_grade = 2
                elif value == 5:
                    response_grade = 1
            elif i==12:
                if value == 1:
                    response_grade = 1
                elif value == 2:
                    response_grade = 2
                elif value == 3:
                    response_grade = 3
                elif value == 4:
                    response_grade = 3
                elif value == 5:
                    response_grade = 4
            elif i==13:
                if value == 1:
                    response_grade = 3
                elif value == 2:
                    response_grade = 4
                elif value == 3:
                    response_grade = 4
                elif value == 4:
                    response_grade = 2
                elif value == 5:
                    response_grade = 1
            elif i==14:
                if value == 1:
                    response_grade = 1
                elif value == 2:
                    response_grade = 4
                elif value == 3:
                    response_grade = 4
                elif value == 4:
                    response_grade = 2
                elif value == 5:
                    response_grade = 3

            setattr(mb_response, f'q{i}', response_grade)
            response_sum += response_grade

        response_avg = response_sum/14
        mb_response.average_score = response_avg
        mb_response.quadrant = math.trunc(response_avg)
        mb_response.save()
        
        return HttpResponse(mb_response.pk)
    else:
        return HttpResponse(-1)


def display_result_view(request, pk):
    mb_response = models.MBResponse.objects.get(pk__exact = pk)
    return render(request, 'mbTest/result_page.html', {'mb_response': mb_response})


def display_results_for_eb_view(request):
    mb_responses = models.MBResponse.objects.all().order_by('name')
    quadrant_dict = {1:0, 2:0, 3:0, 4:0}

    for mbr in mb_responses:
        quadrant_dict[mbr.quadrant] += 1 

    return render(request, 'mbTest/results_for_eb.html', {'mb_responses':mb_responses, 'quadrant_dict': quadrant_dict})