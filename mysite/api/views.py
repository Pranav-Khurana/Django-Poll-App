from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from polls.models import Question
from .serializers import pollsSerializers

@api_view(['GET'])
def pollsList(request):
    queryset = Question.objects.all()
    serializer_class = pollsSerializers(queryset, many=True)
    return Response(serializer_class.data)
