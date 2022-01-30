from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, GenericAPIView

# Create your views here.


# List of all 12 months.
# ----------------------


class MonthsView(ListAPIView):
    queryset = Months.objects.all()
    serializer_class = MonthsSerializer


# List of dates of months.
# ------------------------

class JanuaryView(ListAPIView):
    # queryset = January.objects.values_list('date_pk', flat=True)    # STT error due to this value_list COLUMN_NAMES. use .all() instead of value_list() and use fields=("date_pk") in serializer instead of __all__. Yes make a new serializer for this purpose.
    # serializer_class = JanuarySerializer
    queryset = January.objects.all()
    serializer_class = JanuaryDatesSerializer


class FebruaryView(ListAPIView):
    queryset = February.objects.all()
    serializer_class = FebruaryDatesSerializer


class MarchView(ListAPIView):
    queryset = March.objects.all()
    serializer_class = MarchDatesSerializer


class AprilView(ListAPIView):
    queryset = April.objects.all()
    serializer_class = AprilDatesSerializer


class MayView(ListAPIView):
    queryset = May.objects.all()
    serializer_class = MayDatesSerializer


class JuneView(ListAPIView):
    queryset = June.objects.all()
    serializer_class = JuneDatesSerializer


class JulyView(ListAPIView):
    queryset = July.objects.all()
    serializer_class = JulyDatesSerializer


class AugustView(ListAPIView):
    queryset = August.objects.all()
    serializer_class = AugustDatesSerializer


class SeptemberView(ListAPIView):
    queryset = September.objects.all()
    serializer_class = SeptemberDatesSerializer


class OctoberView(ListAPIView):
    queryset = October.objects.all()
    serializer_class = OctoberDatesSerializer


class NovemberView(ListAPIView):
    queryset = November.objects.all()
    serializer_class = NovemberDatesSerializer


class DecemberView(ListAPIView):
    queryset = December.objects.all()
    serializer_class = DecemberDatesSerializer


# Find time table of whole month.
# ------------------------------


class JanuaryAllView(ListAPIView):
    queryset = January.objects.all()
    serializer_class = JanuarySerializer


class FebruaryAllView(ListAPIView):
    queryset = February.objects.all()
    serializer_class = FebruarySerializer


class MarchAllView(ListAPIView):
    queryset = March.objects.all()
    serializer_class = MarchSerializer


class AprilAllView(ListAPIView):
    queryset = April.objects.all()
    serializer_class = AprilSerializer


class MayAllView(ListAPIView):
    queryset = May.objects.all()
    serializer_class = MaySerializer


class JuneAllView(ListAPIView):
    queryset = June.objects.all()
    serializer_class = JuneSerializer


class JulyAllView(ListAPIView):
    queryset = July.objects.all()
    serializer_class = JulySerializer


class AugustAllView(ListAPIView):
    queryset = August.objects.all()
    serializer_class = AugustSerializer


class SeptemberAllView(ListAPIView):
    queryset = September.objects.all()
    serializer_class = SeptemberSerializer


class OctoberAllView(ListAPIView):
    queryset = October.objects.all()
    serializer_class = OctoberSerializer


class NovemberAllView(ListAPIView):
    queryset = November.objects.all()
    serializer_class = NovemberSerializer


class DecemberAllView(ListAPIView):
    queryset = December.objects.all()
    serializer_class = DecemberSerializer


# Find time table of particular date.
# -----------------------------------

# @api_view(["GET"])
# def JanuarySearchView(request, **kwargs):
#     pk = kwargs.get("pk", None)
#     queryset = January.objects.filter(date_pk=pk).first()
#     serializer = JanuarySerializer(queryset)
#     return Response(serializer.data)


class JanuarySearchView(APIView):
    def get(self, request, pk, *args, **kwargs):
        queryset = January.objects.get(date_pk=pk)
        serializer = JanuarySerializer(queryset)
        return Response(serializer.data)


class FebruarySearchView(APIView):
    def get(self, request, pk, *args, **kwargs):
        queryset = February.objects.get(date_pk=pk)
        serializer = FebruarySerializer(queryset)
        return Response(serializer.data)


class MarchSearchView(APIView):
    def get(self, request, pk, *args, **kwargs):
        queryset = March.objects.get(date_pk=pk)
        serializer = MarchSerializer(queryset)
        return Response(serializer.data)


class AprilSearchView(APIView):
    def get(self, request, pk, *args, **kwargs):
        queryset = April.objects.get(date_pk=pk)
        serializer = AprilSerializer(queryset)
        return Response(serializer.data)


class MaySearchView(APIView):
    def get(self, request, pk, *args, **kwargs):
        queryset = May.objects.get(date_pk=pk)
        serializer = MaySerializer(queryset)
        return Response(serializer.data)


class JuneSearchView(APIView):
    def get(self, request, pk, *args, **kwargs):
        queryset = June.objects.get(date_pk=pk)
        serializer = JuneSerializer(queryset)
        return Response(serializer.data)


class JulySearchView(APIView):
    def get(self, request, pk, *args, **kwargs):
        queryset = July.objects.get(date_pk=pk)
        serializer = JulySerializer(queryset)
        return Response(serializer.data)


class AugustSearchView(APIView):
    def get(self, request, pk, *args, **kwargs):
        queryset = August.objects.get(date_pk=pk)
        serializer = AugustSerializer(queryset)
        return Response(serializer.data)


class SeptemberSearchView(APIView):
    def get(self, request, pk, *args, **kwargs):
        queryset = September.objects.get(date_pk=pk)
        serializer = SeptemberSerializer(queryset)
        return Response(serializer.data)


class OctoberSearchView(APIView):
    def get(self, request, pk, *args, **kwargs):
        queryset = October.objects.get(date_pk=pk)
        serializer = OctoberSerializer(queryset)
        return Response(serializer.data)


class NovemberSearchView(APIView):
    def get(self, request, pk, *args, **kwargs):
        queryset = November.objects.get(date_pk=pk)
        serializer = NovemberSerializer(queryset)
        return Response(serializer.data)


class DecemberSearchView(APIView):
    def get(self, request, pk, *args, **kwargs):
        queryset = December.objects.get(date_pk=pk)
        serializer = DecemberSerializer(queryset)
        return Response(serializer.data)
