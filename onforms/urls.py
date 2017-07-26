from django.conf.urls import url
from .views import CustomBioView

urlpatterns = [
  #url(r'newbio/$',BioView.as_view(),name ='bio'),
  url(r'customnewbio/$',CustomBioView,name='custombio'),

  
]