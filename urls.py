from django.urls import path, include
from django.contrib import admin
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import urls, schemas

admin.site.site_url = '/' + settings.URL_PATH_PREFIX

urlpatterns = [
    path(
        settings.URL_PATH_PREFIX,
        include(
            [
                path('admin/', admin.site.urls),
                path('', include('django.contrib.auth.urls')),
                path('', include('solicitacao.urls', namespace='solicitacao')),
                path('api', schemas.get_schema_view(
                    title="ID - Identidade do usuários",
                    description="API for all things …",
                    version="1.0.0"
                ), name='openapi-schema'),    

                # path('api-auth/', include('rest_framework.urls')),
                # path('logout/', jwt_logout, name='logout'),
                # path('', include('suap_ead.urls', namespace='suap_ead')),
            ]
        )
    ),
    path('', RedirectView.as_view(url=settings.URL_PATH_PREFIX)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(path('%s__debug__/' % settings.URL_PATH_PREFIX, include(debug_toolbar.urls)))
