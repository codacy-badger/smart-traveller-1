from rest_framework import serializers

from transports.models import (
    FleetType, Fleet, Location,
    Route, FleetAssignment
)

class FleetTypeSerializer(serializers.ModelSerializer):
    """
    A Serializer for the fleet type model with all required field.
    """
    class Meta:
        """
        Exposes required model fields.
        """
        model = FleetType
        fields = ('id', 'name', 'status', 'created_by', 'created_at', 'updated_at')

    def create(self, validated_data):
        fleettype = FleetType(**validated_data)
        fleettype.save()

        return fleettype

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()

        return instance


class FleetSerializer(serializers.ModelSerializer):
    """
    A Serializer for the fleet model with all required field.
    """
    class Meta:
        """
        Exposes required model fields.
        """
        model = Fleet
        fields = ('id', 'registration_no', 'engine_no', 'chasis_no', 'model_no', 'fleet_type',
                 'layout', 'seat_nos', 'status', 'created_by', 'created_at', 'updated_at')

    def create(self, validated_data):
        fleet = Fleet(**validated_data)
        fleet.save()

        return fleet

    def update(self, instance, validated_data):
        instance.registration_no = validated_data.get('registration_no', instance.registration_no)
        instance.save()

        return instance


class LocationSerializer(serializers.ModelSerializer):
    """
    A Serializer for the location model with all required field.
    """
    class Meta:
        """
        Exposes required model fields.
        """
        model = Location
        fields = ('id', 'name', 'description', 'status', 'created_by', 'created_at', 'updated_at')

    def create(self, validated_data):
        location = Location(**validated_data)
        location.save()

        return location

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()

        return instance


class RouteSerializer(serializers.ModelSerializer):
    """
    A Serializer for the route model with all required field.
    """
    class Meta:
        """
        Exposes required model fields.
        """
        model = Route
        fields = ('id', 'name', 'start_point', 'end_point', 'stopage_points','distance',
            'approximate_time', 'status', 'created_by', 'created_at', 'updated_at')

    def create(self, validated_data):
        route = Route(**validated_data)
        route.save()

        return route

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()

        return instance


class FleetAssignmentSerializer(serializers.ModelSerializer):
    """
    A Serializer for the route model with all required field.
    """
    class Meta:
        """
        Exposes required model fields.
        """
        model = FleetAssignment
        fields = ('id', 'fleet_registration_no', 'route_name', 'trip_start_date',
                'trip_end_date', 'status', 'created_by', 'created_at', 'updated_at')

    def create(self, validated_data):
        fleet_assignment = FleetAssignment(**validated_data)
        fleet_assignment.save()

        return fleet_assignment

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.save()

        return instance
