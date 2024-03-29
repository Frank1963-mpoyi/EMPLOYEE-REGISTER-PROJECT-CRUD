from django.conf                                                    import settings
from django.conf.urls.static                                        import static
from django.contrib                                                 import admin
from django.urls                                                    import path, include


urlpatterns = [
    path('',                                    include('register.apps.web.urls')),
    path('accounts/',                           include('allauth.urls')),
]

if settings.DEBUG:

    import debug_toolbar
    
    urlpatterns = [
        path('__debug__/',                      include(debug_toolbar.urls)),
        path('admin/',                     admin.site.urls),
        ]+urlpatterns

    urlpatterns += static(settings.STATIC_URL,  document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,   document_root=settings.MEDIA_ROOT)