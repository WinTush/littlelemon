from rest_framework import serializers

from restaurant.models import Booking, Menu


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"
        extra_kwargs = {
            "price": {
                "min_value": 2,
            },
            "inventory": {
                "min_value": 0,
            },
        }


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
