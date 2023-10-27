from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from ..models import MagnetModel
@csrf_exempt
 
 
 
def add_MagnetometerData(request):
        if request.method == 'POST':
            data = json.loads(request.body)
            Magnet_points = [point.split('~') for point in data['magnet_string'].split('|')]
            Magnet_points=Magnet_points[1:len(Magnet_points)]
            templateName=data['templateName']
            longitudenal=data['longi']
            latitudenal=data['lati']
            # Add the template data to the database
            for i in range(len(Magnet_points)):
                    newTemplate = MagnetModel(template_name = templateName, x = Magnet_points[i][0], y = Magnet_points[i][1],z = Magnet_points[i][2], long = longitudenal, lati = latitudenal)
                    newTemplate .save()
       
            return JsonResponse({'success':True,'message': 'Magnetometer Data received successfully'})
        else:
            return JsonResponse({'success':False,'error': 'Invalid request method'}, status=400)