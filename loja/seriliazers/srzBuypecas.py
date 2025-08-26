from rest_framework import serializers
from loja.classes.buyPecas import BuyPecas

class BuyPecasSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyPecas
        fields = '__all__'   