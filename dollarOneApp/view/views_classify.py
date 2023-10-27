from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from ..models import AccelorometerModel
from ..models import MagnetModel
from ..models import GyroModel
from ..models import classifiedTemplates
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw
 
 
 
@csrf_exempt
def classifyTemplate(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        acc_points = [point.split('~') for point in data['input_string'].split('|')]
        acc_points=acc_points[1:len(acc_points)]
        acc_points=[(float(point[0]), float(point[1]),float(point[2])) for point in acc_points ]
 
        gyro_points = [point.split('~') for point in data['gyro_string'].split('|')]
        gyro_points= gyro_points[1:len( gyro_points)]
 
        Mag_points = [point.split('~') for point in data['magnet_string'].split('|')]
        Mag_points= Mag_points[1:len(Mag_points)]
 
        longitudenal=data['longi']
        latitudenal=data['lati']
        try:
            unique_template_names =AccelorometerModel.objects.values_list('template_name', flat=True).distinct()
            templateName=list(unique_template_names)
           
            sensors={'Model':[AccelorometerModel,GyroModel,MagnetModel],
                    'DataPoints':[acc_points,gyro_points,Mag_points]}
            Final_Result={}
            for model, data_points in zip(sensors['Model'], sensors['DataPoints']):
                    Template_points={}
                    for i in range(len(templateName)):
                        points =model.objects.filter(template_name=templateName[i])
                        points_list = [(float(data.x), float(data.y),float(data.z)) for data in points]
                        # Calculate DTW distance and alignment path
                        distance, path = fastdtw(data_points,points_list, dist=euclidean)
                        Template_points[templateName[i]]=distance
                    # Find the template name with the least distance
                    min_distance_template = min(Template_points, key=Template_points.get)
 
                    # Get the distance for the template with the least distance
                    min_distance = Template_points[min_distance_template]
                    Final_Result[model.__name__]=[min_distance_template,min_distance]
 
 
 
            Models=Final_Result.keys()
            templates = [Final_Result[Model][0] for Model in Models]
            processed_templates = set()
            for template in templates:
                    if templates.count(template) >= 2:
                            min_distance=min([Final_Result[Model][1] for Model in Models])
                            alignment_score= 1 / (1 +  min_distance)
                            newTemplate = classifiedTemplates(long = longitudenal, lati =  latitudenal,template_name = template,distance = min_distance,alignment_Score = alignment_score, classified_by =  'Eucledian_Distance')
                            newTemplate.save()
                            return JsonResponse({'success':True,'message': 'Classified Template is added successfully','template_name': template, 'alignment_similarity_score': alignment_score})
                       
                       
                    else:
                        alignment_similarity_score={Model:1 / (1 + Final_Result[Model][1])for Model in Models}
                        max_Key = max(alignment_similarity_score.keys(), key=lambda k: alignment_similarity_score[k])
                        max_similarity =max(max_Key)
                        template=Final_Result[max_Key][0]
                        newTemplate = classifiedTemplates(long = longitudenal, lati = latitudenal,template_name= template, distance = Final_Result[max_Key][1] , alignment_Score = max_similarity, classified_by = 'Alignment_similarity_score')
                        newTemplate.save()
                        return JsonResponse({'success':True,'message': 'Classified Template is added successfully','template_name': template, 'alignment_similarity_score': max_similarity})
                       
                       
        except AccelorometerModel.DoesNotExist or GyroModel.DoesNotExist or MagnetModel.DoesNotExist:
                return JsonResponse({'success':False,'error': 'database not found'}, status=400)
 
 
           
         
    else:
            return JsonResponse({'success':False,'error': 'Invalid request method'}, status=400)