
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import json
# from ..models import AccelorometerModel
# @csrf_exempt
# def add_AccelerometerData(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         acc_points = [point.split('~') for point in data['input_string'].split('|')]
#         acc_points=acc_points[1:len(acc_points)]
#         print(acc_points)
#         templateName=data['templateName']
#         print(templateName)
#         # Add the template data to the database
#         for i in range(len(acc_points)):
#                 newTemplate = AccelorometerModel(i,templateName, acc_points[i][0],acc_points[i][1],acc_points[i][2])
                
#                 newTemplate .save()
   
#         return JsonResponse({'success':True,'message': 'Accelerometer Data received successfully'})
#     else:
#         return JsonResponse({'success':False,'error': 'Invalid request method'}, status=400)



from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from ..models import AccelorometerModel
@csrf_exempt
def add_AccelerometerData(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        acc_points = [point.split('~') for point in data['input_string'].split('|')]
        acc_points=acc_points[1:len(acc_points)]
        templateName=data['templateName']
        longitudenal=data['longi']
        latidudenal=data['lati']
        # Add the template data to the database
        for i in range(len(acc_points)):
                newTemplate = AccelorometerModel(template_name = templateName, x = acc_points[i][0], y = acc_points[i][1], z = acc_points[i][2], longi = longitudenal, lati = latidudenal)
                newTemplate .save()
   
        return JsonResponse({'success':True,'message': 'Accelerometer Data received successfully'})
    else:
        return JsonResponse({'success':False,'error': 'Invalid request method'}, status=400)