from rest_framework.filters import OrderingFilter
from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet


from users.models import Payments
from users.serializers import PaymentsSerializers, UserSerializer



class PaymentsViewSet(ModelViewSet):
    serializer_class = PaymentsSerializers
    queryset = Payments.objects.all()
    filter_backends = [OrderingFilter]
    filterset_fields = ['course', 'lesson', 'payment_method']
    ordering_fields = ['date']


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
