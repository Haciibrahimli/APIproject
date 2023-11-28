from django.urls import path
from my_app.views import *

urlpatterns = [
    path("", GYMListView.as_view(), name='gym-list'),
    path("gymcreated/", GYMCreateAPIView.as_view(), name='gym-created'),
    path("gymupdate/<id>/", GYMUpdateAPIView.as_view(), name='update'),
    path("gym/<id>/", GYMRetrieveAPIView.as_view(), name='detail'),
    path("gymdelate/<id>/", GYMDestroyAPIView.as_view(), name='delate'),

]