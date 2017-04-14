from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
	# /music/
	url(r'^stocks/$', views.StockList.as_view())
]
