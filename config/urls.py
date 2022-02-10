from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
#from common import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',views.signup, name="signup"),
    path('', include('common.urls'),name='index'),
    path('dailyphoto/',include('dailyphoto.urls'))

]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

