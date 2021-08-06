"""basmango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.permissions import BasePermission,IsAuthenticated,SAFE_METHODS
from supplychain.models import MangoFarm;
from supplychain.models  import Customer;
class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        
        return request.method in SAFE_METHODS

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ['customer_name','mango_requirement','x_coord','y_coord','city']
        
# ViewSets define the view behavior.
class CustomerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
  

class FarmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MangoFarm
        fields = ['farm_name','max_mangos','x_coord','y_coord']
        
# ViewSets define the view behavior.
class FarmViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MangoFarm.objects.all()
    serializer_class = FarmSerializer
    
router = routers.DefaultRouter()
router.register(r'farms', FarmViewSet)
router.register(r'customers', CustomerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
