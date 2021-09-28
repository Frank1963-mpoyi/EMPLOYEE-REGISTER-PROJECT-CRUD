from django.urls                                                    import path, include


urlpatterns = [
    path('',                                    include('register.apps.web.blog.urls')),

]
