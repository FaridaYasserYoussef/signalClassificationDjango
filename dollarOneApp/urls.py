from django.urls import path
# from .view.views_receive import receive_accelerometer_data
from .view.views_classify import classifyTemplate
from .view.views_addAcc import add_AccelerometerData
from .view.views_addGYRO import add_GyroscopeData
from .view.views_addMag import add_MagnetometerData
urlpatterns = [
    # path('receive-accelerometer-data/', receive_accelerometer_data, name='receive_accelerometer_data'),
    path('add_AccelerometerData/', add_AccelerometerData, name='add_AccelerometerData'),
    path('add_GyroscopeData/', add_GyroscopeData, name='add_GyroscopeData'),
    path('add_MagnetometerData/', add_MagnetometerData, name='add_MagnetometerData'),
    path('classifyTemplate/', classifyTemplate, name='classifyTemplate'),
]  