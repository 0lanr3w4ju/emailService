from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework.response import Response

from emailService.serializers import ContactUsSerializer

# Create your views here.

@api_view(['POST'])
def send_mail_view(request, *args, **kwargs):

    contactus_serializer = ContactUsSerializer(data=request.data)

    if contactus_serializer.is_valid(raise_exception=True):
        client_data = contactus_serializer.data

        send_mail(
            'CARLIE CLIENT FORM', 
            f'Hi, {client_data["first_name"]} {client_data["last_name"]} is available on {client_data["available_date"]}',
            client_data["email"],
            ['olanr3wajualawode@gmail.com'],
            fail_silently=False
        )        
        return Response('_sent_')
    
    else:
        return Response('_unknown_request_')
