import os
import django
import pandas as pd

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'f1_project.settings')
django.setup()

from f1_app.models import Circuit, Constructor, Driver, Race, Result, Season, Status

def load_circuits():
    Circuit.objects.all().delete()
    df = pd.read_csv('data_files/circuits.csv')
    for _, row in df.iterrows():
        Circuit.objects.create(
            circuitId=row['circuitId'],
            circuitRef=row['circuitRef'],
            name=row['name'],
            location=row['location'],
            country=row['country'],
            lat=row['lat'],
            lng=row['lng'],
            alt=row['alt'],
            url=row['url']
        )

def load_constructors():
    Constructor.objects.all().delete()
    df = pd.read_csv('data_files/constructors.csv')
    for _, row in df.iterrows():
        Constructor.objects.create(
            constructorId=row['constructorId'],
            constructorRef=row['constructorRef'],
            name=row['name'],
            nationality=row['nationality'],
            url=row['url']
        )

def load_drivers():
    Driver.objects.all().delete()
    df = pd.read_csv('data_files/drivers.csv')
    for _, row in df.iterrows():
        Driver.objects.create(
            driverId=row['driverId'],
            driverRef=row['driverRef'],
            number=row['number'],
            code=row['code'],
            forename=row['forename'],
            surname=row['surname'],
            dob=pd.to_datetime(row['dob']).date(),
            nationality=row['nationality'],
            url=row['url']
        )

def load_status():
    Status.objects.all().delete()
    df = pd.read_csv('data_files/status.csv')
    for _, row in df.iterrows():
        Status.objects.create(
            statusId=row['statusId'],
            status=row['status']
        )

def load_seasons():
    Season.objects.all().delete()
    df = pd.read_csv('data_files/seasons.csv')
    for _, row in df.iterrows():
        Season.objects.create(
            year=row['year'],
            url=row['url']
        )

def load_races():
    Race.objects.all().delete()
    df = pd.read_csv('data_files/races.csv')
    for _, row in df.iterrows():
        circuit_instance = Circuit.objects.get(circuitId=row['circuitId'])
        Race.objects.create(
            raceId=row['raceId'],
            year=row['year'],
            round=row['round'],
            circuit=circuit_instance,
            name=row['name'],
            date=pd.to_datetime(row['date']).date(),
            time=row['time'],
            url=row['url'],
            fp1_date=row['fp1_date'],
            fp1_time=row['fp1_time'],
            fp2_date=row['fp2_date'],
            fp2_time=row['fp2_time'],
            fp3_date=row['fp3_date'],
            fp3_time=row['fp3_time'],
            quali_date=row['quali_date'],
            quali_time=row['quali_time'],
            sprint_date=row['sprint_date'],
            sprint_time=row['sprint_time']
        )

def load_results():
    Result.objects.all().delete()
    df = pd.read_csv('data_files/results.csv')
    for _, row in df.iterrows():
        try:
            race_instance = Race.objects.get(raceId=row['raceId'])
            driver_instance = Driver.objects.get(driverId=row['driverId'])
            constructor_instance = Constructor.objects.get(constructorId=row['constructorId'])
            status_instance = Status.objects.get(statusId=row['statusId'])
        except (Race.DoesNotExist, Driver.DoesNotExist, Constructor.DoesNotExist, Status.DoesNotExist) as e:
            print(f"Referenced record does not exist: {e}. Skipping result {row['resultId']}.")
            continue

        Result.objects.create(
            resultId=row['resultId'],
            race=race_instance,
            driver=driver_instance,
            constructor=constructor_instance,
            number=row['number'],
            grid=row['grid'],
            position=row['position'],
            positionText=row['positionText'],
            positionOrder=row['positionOrder'],
            points=row['points'],
            laps=row['laps'],
            time=row['time'],
            milliseconds=row['milliseconds'],
            fastestLap=row['fastestLap'],
            rank=row['rank'],
            fastestLapTime=row['fastestLapTime'],
            fastestLapSpeed=row['fastestLapSpeed'],
            status=status_instance
        )

def main():
    load_circuits()
    load_constructors()
    load_drivers()
    load_status()
    load_seasons()
    load_races()
    load_results()


if __name__ == '__main__':
    main()
