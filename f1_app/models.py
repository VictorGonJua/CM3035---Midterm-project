from django.db import models

# Create your models here.

class Circuit(models.Model):
    circuitId = models.AutoField(primary_key=True)
    circuitRef = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    lat = models.FloatField()
    lng = models.FloatField()
    alt = models.CharField(max_length=255)
    url = models.CharField(max_length=255, default="")

class Constructor(models.Model):
    constructorId = models.AutoField(primary_key=True)
    constructorRef = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    url = models.CharField(max_length=255, default="")


class Driver(models.Model):
    driverId = models.AutoField(primary_key=True)
    driverRef = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    forename = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    dob = models.DateField()
    nationality = models.CharField(max_length=255)
    url = models.CharField(max_length=255, default="")

class Status(models.Model):
    statusId = models.AutoField(primary_key=True)
    status = models.CharField(max_length=255)

class Race(models.Model):
    raceId = models.AutoField(primary_key=True)
    year = models.IntegerField()
    round = models.IntegerField()
    circuit = models.ForeignKey(Circuit, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    date = models.DateField()
    time = models.CharField(max_length=255, null=True, blank=True)  # If some races don't have times
    url = models.CharField(max_length=255, default="")
    fp1_date = models.CharField(max_length=255, null=True, blank=True)
    fp1_time = models.CharField(max_length=255, null=True, blank=True)
    fp2_date = models.CharField(max_length=255, null=True, blank=True)
    fp2_time = models.CharField(max_length=255, null=True, blank=True)
    fp3_date = models.CharField(max_length=255, null=True, blank=True)
    fp3_time = models.CharField(max_length=255, null=True, blank=True)
    quali_date = models.CharField(max_length=255, null=True, blank=True)
    quali_time = models.CharField(max_length=255, null=True, blank=True)
    sprint_date = models.CharField(max_length=255, null=True, blank=True)
    sprint_time = models.CharField(max_length=255, null=True, blank=True)


class Result(models.Model):
    resultId = models.AutoField(primary_key=True)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    constructor = models.ForeignKey(Constructor, on_delete=models.CASCADE)
    number = models.CharField(max_length=255, null=True, blank=True)
    grid = models.IntegerField()
    position = models.CharField(max_length=255, null=True, blank=True)
    positionText = models.CharField(max_length=255)
    positionOrder = models.IntegerField()
    points = models.FloatField()
    laps = models.IntegerField()
    time = models.CharField(max_length=255, null=True, blank=True)
    milliseconds = models.CharField(max_length=255, null=True, blank=True)
    fastestLap = models.CharField(max_length=255, null=True, blank=True)
    rank = models.CharField(max_length=255, null=True, blank=True)
    fastestLapTime = models.CharField(max_length=255, null=True, blank=True)
    fastestLapSpeed = models.CharField(max_length=255, null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)


class Season(models.Model):
    year = models.IntegerField(primary_key=True)
    url = models.CharField(max_length=255, default="")


