from rest_framework import serializers

from restaurant.models import Menu


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
