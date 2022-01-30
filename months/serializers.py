from rest_framework import serializers
from .models import *


class MonthsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Months
        fields = "__all__"  # Use all attributs in model.py


class JanuaryDatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = January
        fields = ("date_pk",)


class FebruaryDatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = February
        fields = ("date_pk",)


class MarchDatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = March
        fields = ("date_pk",)


class AprilDatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = April
        fields = ("date_pk",)


class MayDatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = May
        fields = ("date_pk",)


class JuneDatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = June
        fields = ("date_pk",)


class JulyDatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = July
        fields = ("date_pk",)


class AugustDatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = August
        fields = ("date_pk",)


class SeptemberDatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = September
        fields = ("date_pk",)


class OctoberDatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = October
        fields = ("date_pk",)


class NovemberDatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = November
        fields = ("date_pk",)


class DecemberDatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = December
        fields = ("date_pk",)


class JanuarySerializer(serializers.ModelSerializer):
    class Meta:
        model = January
        fields = "__all__"


class FebruarySerializer(serializers.ModelSerializer):
    class Meta:
        model = February
        fields = "__all__"


class MarchSerializer(serializers.ModelSerializer):
    class Meta:
        model = March
        fields = "__all__"


class AprilSerializer(serializers.ModelSerializer):
    class Meta:
        model = April
        fields = "__all__"


class MaySerializer(serializers.ModelSerializer):
    class Meta:
        model = May
        fields = "__all__"


class JuneSerializer(serializers.ModelSerializer):
    class Meta:
        model = June
        fields = "__all__"


class JulySerializer(serializers.ModelSerializer):
    class Meta:
        model = July
        fields = "__all__"


class AugustSerializer(serializers.ModelSerializer):
    class Meta:
        model = August
        fields = "__all__"


class SeptemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = September
        fields = "__all__"


class OctoberSerializer(serializers.ModelSerializer):
    class Meta:
        model = October
        fields = "__all__"


class NovemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = November
        fields = "__all__"


class DecemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = December
        fields = "__all__"
