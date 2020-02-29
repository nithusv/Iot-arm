from rest_framework import serializers
from main.models import Mode

class ModeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mode
        fields = ('mode_id','led','servo_1','servo_2','servo_3','servo_4')
