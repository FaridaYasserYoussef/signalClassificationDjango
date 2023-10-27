from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from ..models import AccelorometerModel
from dollarpy import Recognizer, Point,Template

@csrf_exempt
def receive_accelerometer_data(request):
    print('first few characters=<{}>'.format(request.body[:4]))

    if request.method == 'POST':
        data = json.loads(request.body)
        points = [point.split('~') for point in data['input_string'].split('|')]
        points=points[1:len(points)]
        try:
        # Retrieve all points from the database 
            unique_template_names =AccelorometerModel.objects.values_list('template_name', flat=True).distinct()
            templateName=list(unique_template_names)
            Templates=[]
            for i in range(len(templateName)):
                data_points =AccelorometerModel.objects.filter(template_name=templateName[i])
                points_list = [(data.x, data.y) for data in data_points]
                print(points_list)
                pointObjectlist= [Point(float(point[0]), float(point[1])) for point in points_list]
                Templates.append(Template(templateName[i],pointObjectlist))
            # Use Dollarpy to classify the template
            # Create a 'Recognizer' object and pass the created 'Template' objects as a list.
            recognizer = Recognizer(Templates) 
            # These 'Point' elements have 'x' and 'y' coordinates 
            Accelerometer_points= [Point(float(point[0]), float(point[1])) for point in points]
            # Call 'recognize(...)' to match a list of 'Point' elements to the previously defined templates.
            result = recognizer.recognize(Accelerometer_points)
            gesture_name = result[0]
            probability = result[1]
            print(gesture_name)

            return JsonResponse({'success':True,'message': 'Data received successfully','template_name': gesture_name, 'probability': probability})
        except AccelorometerModel.DoesNotExist:
                return JsonResponse({'success':False,'error': 'database not found'}, status=400)

        
    else:
        return JsonResponse({'success':False,'error': 'Invalid request method'}, status=400)
    
