from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app1.urls')),
    path('predict/', include('app1.urls')),
    path('/about/',include('app1.urls'))
]