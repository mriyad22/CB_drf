from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PersonModel
from .serializers import PersionSerializer


class PersionApiView(APIView):
#----------> Create Data
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

    
#---------> Display Data
    def get_object(self, pk): 
        try:
            return PersonModel.objects.get(id = pk)
        except PersonModel.DoesNotExist:
            return Response({
                "success" : False,
                "message" : "You are a bad guy"
            }, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request, pk=None):
        if not pk:
            user_data = PersonModel.objects.all()
            serializer = PersionSerializer(user_data, many=True)
    
            return Response({
                "success" : True,
                "message" : "data get",
                "data" : serializer.data
            }, status=status.HTTP_200_OK)
        else:
            user_data = self.get_object(pk)
            serializer = PersionSerializer(user_data)

            return Response({
                "success" : True,
                "message" : "Individual data get",
                "data" : serializer.data
            }, status=status.HTTP_200_OK)



    def put(self, request, pk):
        updata_data = self.get_object(pk)
        serializer = PersionSerializer(updata_data, data = request.data)
        if serializer.is_valid():
            serializer.save()

            return Response({
                "success" : True,
                "message" : "data updated",
                "data" : serializer.data
            }, status=status.HTTP_201_CREATED)


    def delete(self, request, pk):
        delete_data = self.get_object(pk)
        delete_data.delete()
        return Response({
            "success" : True,
            "message" : "Data deleted",
        }, status=status.HTTP_200_OK) 


