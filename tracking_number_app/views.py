from django.core.cache import cache
from django.db import IntegrityError, transaction
from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import TrackingNumber
from .serializers import TrackingNumberSerializer
from .utils import generate_tracking_number

class ParcelTrackingView(APIView):
    def get(self, request):
        serializer = TrackingNumberSerializer(data=request.query_params)

        if serializer.is_valid():
            validated_data = serializer.validated_data
            while True:
                try:
                    tracking_number = generate_tracking_number(validated_data)
                    created_at = timezone.now().isoformat()

                    # Check tracking number exists in cache
                    if cache.get(tracking_number):
                        continue

                    with transaction.atomic():
                        # Create tracking number object
                        TrackingNumber.objects.create(
                            tracking_number=tracking_number,
                            origin_country_id = validated_data['origin_country_id'],
                            destination_country_id = validated_data['destination_country_id'],
                            weight = validated_data['weight'],
                            customer_id = validated_data['customer_id'],
                            customer_name = validated_data['customer_name']
                        )

                        # Set the tracking number in cache with 1 hour duration
                        cache.set(tracking_number, True, timeout=3600)

                        return Response({
                            'tracking_number': tracking_number,
                            'created_at': created_at
                        }, status=status.HTTP_200_OK)

                except IntegrityError:
                    continue

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
