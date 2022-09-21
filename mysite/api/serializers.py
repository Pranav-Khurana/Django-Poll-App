from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers
from polls.models import Question,Choice

class pollsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ['question_text']