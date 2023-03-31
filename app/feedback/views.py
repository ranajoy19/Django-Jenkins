from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import FeedBack
from .serializers import createfeedBack
import pandas
import csv

@api_view(["POST"])
def create_feedback(request):
    try:
        s = createfeedBack(data=request.data)
        if not s.is_valid():
            return Response({
                "status":False,
                "error":s.errors
            })

        FeedBack.objects.create(**s.validated_data)

        feedback =  FeedBack.objects.all()

        s = createfeedBack(feedback,many=True)

        return Response({
            "status":True,
            "message":"feedback stored successfully",
            "data":s.data
        })
            
    except BaseException as err:
        return Response({
                        "status":False,
                        "error":err
                    })


@api_view(["GET"])
def download_as_cvs(request):
    try:
        feedbacks =  list(FeedBack.objects.all().values_list('name','phone_number'))
        response = HttpResponse (content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="file.csv"'                                
        writer =csv.writer(response)
        writer.writerow(["NAME",'PHONE'])
        for field in feedbacks:
            writer.writerow(field)
        return response

    except BaseException as err:
        return Response({
                        "status":False,
                        "error":err
                    })
