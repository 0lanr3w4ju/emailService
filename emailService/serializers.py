from rest_framework import serializers
from emailService.models import ContactUsModel

class ContactUsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ContactUsModel
        fields = ['first_name', 'last_name', 'email', 'phone_no', 'service_loc', 'available_date']