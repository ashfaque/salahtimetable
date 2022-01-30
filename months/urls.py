from django.urls import path
from django.conf.urls import url
from . import views    # . ---> current working dir
from .views import *

# from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    # :::::::::: List of all 12 months ::::::::::
    path('api/months/',views.MonthsView.as_view()),

    # :::::::::: List of all dates of months ::::::::::     ERROR
    path('api/months/january/',views.JanuaryView.as_view()),
    path('api/months/february/',views.FebruaryView.as_view()),
    path('api/months/march/',views.MarchView.as_view()),
    path('api/months/april/',views.AprilView.as_view()),
    path('api/months/may/',views.MayView.as_view()),
    path('api/months/june/',views.JuneView.as_view()),
    path('api/months/july/',views.JulyView.as_view()),
    path('api/months/august/',views.AugustView.as_view()),
    path('api/months/september/',views.SeptemberView.as_view()),
    path('api/months/october/',views.OctoberView.as_view()),
    path('api/months/november/',views.NovemberView.as_view()),
    path('api/months/december/',views.DecemberView.as_view()),

    # :::::::::: Time table of whole month ::::::::::
    path('api/months/january/all/',views.JanuaryAllView.as_view()),
    path('api/months/february/all/',views.FebruaryAllView.as_view()),
    path('api/months/march/all/',views.MarchAllView.as_view()),
    path('api/months/april/all/',views.AprilAllView.as_view()),
    path('api/months/may/all/',views.MayAllView.as_view()),
    path('api/months/june/all/',views.JuneAllView.as_view()),
    path('api/months/july/all/',views.JulyAllView.as_view()),
    path('api/months/august/all/',views.AugustAllView.as_view()),
    path('api/months/september/all/',views.SeptemberAllView.as_view()),
    path('api/months/october/all/',views.OctoberAllView.as_view()),
    path('api/months/november/all/',views.NovemberAllView.as_view()),
    path('api/months/december/all/',views.DecemberAllView.as_view()),

    #  :::::::::: Time table of particular date ::::::::::
    # path('months/january/<pk>/',views.JanuarySearchView),                 # If using function based view.
    path('api/months/january/<pk>/',views.JanuarySearchView.as_view()),         # If using class based view.
    path('api/months/february/<pk>/',views.FebruarySearchView),
    path('api/months/march/<pk>/',views.MarchSearchView),
    path('api/months/april/<pk>/',views.AprilSearchView),
    path('api/months/may/<pk>/',views.MaySearchView),
    path('api/months/june/<pk>/',views.JuneSearchView),
    path('api/months/july/<pk>/',views.JulySearchView),
    path('api/months/august/<pk>/',views.AugustSearchView),
    path('api/months/september/<pk>/',views.SeptemberSearchView),
    path('api/months/october/<pk>/',views.OctoberSearchView),
    path('api/months/november/<pk>/',views.NovemberSearchView),
    path('api/months/december/<pk>/',views.DecemberSearchView),
]