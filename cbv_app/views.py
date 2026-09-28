from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PersonModel
from .serializers import PersionSerializer


class PersionApiView(APIView):
    def post(self, request):
        serializer_data = PersionSerializer(data = request.data)
        if serializer_data.is_valid():
            serializer_data.save()

            return Response({
                "success" : True,
                "message" : "data created",
                "data" : serializer_data.data
            }, status=status.HTTP_201_CREATED)

        return Response({
            "success" : False,
            "message" : serializer_data.errors
        })


    def get(self, request):
        user_data = PersonModel.objects.all()
        serializer = PersionSerializer(user_data, many=True)

        return Response({
            "success" : True,
            "message" : "data get",
            "data" : serializer.data
        }, status=status.HTTP_200_OK)



class PersionDetailApiView(APIView):
    def get_object(self, pk): 
        try:
            return PersonModel.objects.get(id = pk)
        except PersonModel.DoesNotExist:
            return None


    def get(self, request, pk):
        user_data = self.get_object(pk)
        if user_data:
            serializer = PersionSerializer(user_data)

            return Response({
                "success" : True,
                "message" : "Individual data get",
                "data" : serializer.data
            }, status=status.HTTP_200_OK)

        else:
            return Response({
                "success" : False,
                "message" : "You are a bad guy"
            }, status=status.HTTP_400_BAD_REQUEST)
            
