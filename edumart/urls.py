from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


from edumart import views, settings

urlpatterns = [
                  path('', include('social_django.urls', namespace='social')),
                  path('logout/', views.logout, name='logout'),
                  path('admin/', admin.site.urls),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
              static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
