from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Vehicle
from .serializers import VehicleSerializer
from django.shortcuts import render, get_object_or_404
from rest_framework.generics import ListCreateAPIView


# creating api using FBV
# fetch data from list or id
@api_view(['GET'])
def vehicle_list(request):
    vehicle = Vehicle.objects.all()
    serialzer = VehicleSerializer(vehicle, many=True)

    return Response(serialzer.data)


@api_view(['GET'])
def get_vehicle(request, pk):
    vehicle = Vehicle.objects.get(pk=pk)
    serialzer = VehicleSerializer(vehicle)

    return Response(serialzer.data)


# Create vehicle data
@api_view(['POST'])
def create_vehicle(request):
    serialzer = VehicleSerializer(data=request.data)

    if serialzer.is_valid():
        serialzer.save()
        return Response(serialzer.data, status=201)

    return Response(serialzer.errors, status=400)


# modify or replace vehicle data
@api_view(['PUT', 'PATCH'])
def update_vehicle(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)

    serializer = VehicleSerializer(
        vehicle,
        data=request.data,
        partial=request.method == 'PATCH'
    )

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)

    return Response(serializer.errors, status=400)


# delete vehicle data
@api_view(['DELETE'])
def delete_vehicle(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)

    vehicle.delete()

    return Response(
        {"message": f"vehicle with id: {pk} deleted succesfully"},
        status=204
    )


# creating api using CBV
class VehicleListCreateView(ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
