from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count, Min, Max, F
from .models import *
from .serializers import *

class CircuitListView(generics.ListAPIView):
    queryset = Circuit.objects.all()
    serializer_class = CircuitSerializer

class CircuitDetailView(generics.RetrieveAPIView):
    queryset = Circuit.objects.all()
    serializer_class = CircuitSerializer
    lookup_field = 'circuitId'

class RaceListByYearView(generics.ListAPIView):
    serializer_class = RaceSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned races to a given year,
        by filtering against a `year` query parameter in the URL.
        """
        queryset = Race.objects.all()
        year = self.kwargs.get('year')
        if year is not None:
            queryset = queryset.filter(year=year)
        return queryset
    
class DriverSummaryView(APIView):
    def get(self, request, driverId):
        # Get the driver's basic info
        try:
            driver = Driver.objects.get(driverId=driverId)
        except Driver.DoesNotExist:
            return Response({'error': 'Driver not found'}, status=404)
        # Aggregate career summary data
        career_summary = Result.objects.filter(driver_id=driverId).aggregate(
            wins=Count('resultId', filter=F('positionOrder') == 1),
            teams=Count('constructor_id', distinct=True),
            first_year=Min('race__year'),
            last_year=Max('race__year'),
        )
        # Construct the response data
        response_data = {
            'driverId': driverId,
            'driverRef': driver.driverRef,
            'forename': driver.forename,
            'surname': driver.surname,
            'code': driver.code,
            'nationality': driver.nationality,
            'dob': driver.dob,
            'wins': career_summary['wins'],
            'teams': career_summary['teams'],
            'first_year': career_summary['first_year'],
            'last_year': career_summary['last_year']
        }
        return Response(response_data)
    
class DriverListView(generics.ListAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

class DriverCreateView(generics.CreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DriverUpdateView(generics.UpdateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    lookup_field = 'driverId'
    def put(self, request, *args, **kwargs):
        driver = self.get_object()
        serializer = self.get_serializer(driver, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DriverDeleteView(generics.DestroyAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    lookup_field = 'driverId'
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)