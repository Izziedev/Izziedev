
from django.contrib import admin
from django.urls import include,path, re_path


urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'management/',include('management.urls'))
]
