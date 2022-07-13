from django.urls import path,include
from .views import languageApi,FileView,FileViewjson
from . import views

urlpatterns = [
	path('language', languageApi.as_view(), name='trans'),
	path('jsondata', FileView.as_view(), name='jsondata'),
	path('json', FileViewjson.as_view(), name='json'),
]