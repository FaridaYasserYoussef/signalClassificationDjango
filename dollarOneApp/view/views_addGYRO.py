# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import json
# from ..models import GyroModel
# @csrf_exempt
 
 
 
# def add_GyroscopeData(request):
#         if request.method == 'POST':
#             data = json.loads(request.body)
#             GYRO_points = [point.split('~') for point in data['gyro_string'].split('|')]
#             GYRO_points=GYRO_points[1:len(GYRO_points)]
#             templateName=data['templateName']
#             # Add the template data to the database
#             for i in range(len(GYRO_points)):
#                     newTemplate = GyroModel(i,templateName,GYRO_points[i][0],GYRO_points[i][1],GYRO_points[i][2])
#                     newTemplate .save()
       
#             return JsonResponse({'success':True,'message': 'Gyroscope Data received successfully'})
#         else:
#             return JsonResponse({'success':False,'error': 'Invalid request method'}, status=400)



from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from ..models import GyroModel
@csrf_exempt
 
 
 
def add_GyroscopeData(request):
        if request.method == 'POST':
            data = json.loads(request.body)
            GYRO_points = [point.split('~') for point in data['gyro_string'].split('|')]
            GYRO_points=GYRO_points[1:len(GYRO_points)]
            templateName=data['templateName']
            longitudenal=data['longi']
            latidudenal=data['lati']
            # Add the template data to the database
            for i in range(len(GYRO_points)):
                    newTemplate = GyroModel(template_name = templateName,x = GYRO_points[i][0], y = GYRO_points[i][1],z = GYRO_points[i][2],longi = longitudenal, lati = latidudenal)
                    newTemplate .save()
       
            return JsonResponse({'success':True,'message': 'Gyroscope Data received successfully'})
        else:
            return JsonResponse({'success':False,'error': 'Invalid request method'}, status=400)