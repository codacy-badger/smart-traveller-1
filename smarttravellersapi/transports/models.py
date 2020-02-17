from django.db import models
from accounts.models import CustomUser

class FleetType(models.Model):
    """
    Model for tracking service types i.e universal or premium.
    """
    name = models.CharField(max_length=50, unique=True)
    status = models.BooleanField(default=False)
    created_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Fleet(models.Model):
    """
    Model for tracking buses.
    """
    registration_no = models.CharField(max_length=50, unique=True)
    engine_no = models.CharField(max_length=50, unique=True)
    chasis_no = models.CharField(max_length=50, unique=True)
    model_no = models.CharField(max_length=50, unique=True)
    fleet_type = models.ForeignKey(FleetType, on_delete=models.DO_NOTHING)
    layout = models.CharField(max_length=5, unique=False)
    seat_nos = models.IntegerField(null=False)
    status = models.BooleanField(default=False)
    created_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.registration_no


class Location(models.Model):
    """
    Model for tracking trip destinations.
    """
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=100, null=False)
    status = models.BooleanField(default=False)
    created_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Route(models.Model):
    """
    Model for registering trip routes.
    """
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=100, null=False, default="start to destination of trip")
    start_point = models.CharField(max_length=50, unique=False)
    end_point = models.CharField(max_length=50, unique=False)
    stopage_points = models.CharField(max_length=50, unique=False)
    distance = models.FloatField(null=False)
    approximate_time = models.DurationField(null=False, default='08:00:00')
    status = models.BooleanField(default=False)
    created_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class FleetAssignment(models.Model):
    """
    Model for tracking fleet assignment for each route.
    """
    fleet_registration_no = models.ForeignKey(Fleet, on_delete=models.DO_NOTHING)
    route_name = models.ForeignKey(Route, on_delete=models.DO_NOTHING)
    trip_start_date = models.DateTimeField(null=False)
    trip_end_date = models.DateTimeField(null=False)
    status = models.BooleanField(default=False)
    created_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return " {} {} ".format(self.fleet_registration_no, self.route_name)

