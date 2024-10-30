from rest_framework import views
from rest_framework.permissions import AllowAny

class HelloView(views.APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        return views.Response({'message': 'Server is up and running!'})