from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Hotel
from .serializers import HotelSerializers
# from drf.utils import extend_schema 
# from rest_framework.schemas import AutoSchema
# import coreapi
# from drf_spectacular.utils import extend_schema
from drf_yasg.utils import swagger_auto_schema


# class HotelSchema(AutoSchema):
#     def get_fields(self,path,method):
#         extra_fields = []
#         if method.lower() in ['post','put']:
#             extra_fields=[
#                 coreapi.Field('name','email','address','phone_no')
#             ]
#             manual_fields=super().get_fields(path,method)
#             return manual_fields+extra_fields


# @extend_schema(request=HotelSerializers)
class Hotel_List(APIView):
    # schema=HotelSchema()
    def get(self, request):
        details = Hotel.objects.all()
        serializer = HotelSerializers(details, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=HotelSerializers)
    def post(self, request):
        serializer = HotelSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class Hotel_Detail(APIView):
    # schema=HotelSchema()
    def get(self, requests, pk):
        try:
            hotel_detail = Hotel.objects.get(pk=pk)
            serializer = HotelSerializers(hotel_detail)
            return Response(serializer.data)
        except:
            return Response({'errors': 'Details not found'}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=HotelSerializers)
    def put(self, request, pk):
        hotel_detail = Hotel.objects.get(pk=pk)
        serializer = HotelSerializers(hotel_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        hotel_detail = Hotel.objects.get(pk=pk)
        if hotel_detail.delete():
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
