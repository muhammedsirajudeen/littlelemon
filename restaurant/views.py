from django.shortcuts import render
from django.http import HttpResponse


from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

from .serializers import MenuSerializer,BookingSerializer
from .models import Menu,Booking

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


# Create your views here.
def index(request):
    return render(request,'index.html',{})

class MenuItemView(ListCreateAPIView):
    queryset=Menu.objects.all()
    serializer_class=MenuSerializer


class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset=Menu.objects.all()
    serializer_class=MenuSerializer



class BookingViewSet(ModelViewSet):
    permission_classes=[IsAuthenticated]
    queryset=Booking.objects.all()
    serializer_class=BookingSerializer


