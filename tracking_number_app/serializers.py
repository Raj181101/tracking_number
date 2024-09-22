from rest_framework import serializers

class TrackingNumberSerializer(serializers.Serializer):
    origin_country_id = serializers.CharField(max_length=2)
    destination_country_id = serializers.CharField(max_length=2)
    weight = serializers.DecimalField(max_digits=5, decimal_places=3)
    customer_id = serializers.UUIDField()
    customer_name = serializers.CharField(max_length=255)
