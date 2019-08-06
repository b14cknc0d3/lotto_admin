from dynamic_rest import serializers
from dynamic_rest import fields
from .models import *


class UserSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = User

        fields = ('id', 'username', 'email', 'phone', 'address')


class OneLSerializer(serializers.DynamicModelSerializer):
    reseller = fields.DynamicField(source='reseller.username', read_only=True)

    class Meta:
        model = OneL
        fields = (
            'id', 'lno', 'reseller', 'phone', 'address', 'nth', 'is_winner', 'prize_details', 'created_at',
            'updated_at')


class FiveLSerializer(serializers.DynamicModelSerializer):
    reseller = fields.DynamicField(source='reseller.username', read_only=True)

    class Meta:
        model = FiveL
        fields = (
            'id', 'lno', 'reseller', 'phone', 'address', 'nth', 'is_winner', 'prize_details', 'created_at',
            'updated_at')


class TwoLSerializer(serializers.DynamicModelSerializer):
    reseller = fields.DynamicField(source='reseller.username', read_only=True)

    class Meta:
        model = TwoL
        fields = (
            'id', 'lno', 'reseller', 'phone', 'address', 'nth', 'is_winner', 'prize_details', 'created_at',
            'updated_at')
