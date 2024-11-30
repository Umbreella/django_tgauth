from django.urls import include, path


urlpatterns = [
    path('v1.0/', include('src_back.api.private.v1.urls')),
]
