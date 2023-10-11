
"""
URL configuration for Users project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# schema_view = get_schema_view(
#     openapi.Info(
#         title="Content Section and Account Section APIs ",
#         default_version='v1',
#         description="All content section and account section APIs along with their functionalities are given below.",
#         terms_of_service="https://www.yourapi.com/terms/",
#         contact=openapi.Contact(email="contact@yourapi.com"),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )
# )
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('accounts.urls')),
#     path('api/', include('course.urls')),  # Replace 'yourapp.urls' with your API's URL configuration.
#     re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
#     path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#     path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

# ]

schema_view_accounts = get_schema_view(
    openapi.Info(
        title="Accounts and Course APIs",
        default_version='v1',
        description="APIs for the accounts and course app.",
        terms_of_service="https://www.yourapi.com/terms/",
        contact=openapi.Contact(email="contact@yourapi.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
)

# schema_view_course = get_schema_view(
#     openapi.Info(
#         title="Course APIs",
#         default_version='v1',
#         description="APIs for the course app.",
#         terms_of_service="https://www.yourapi.com/terms/",
#         contact=openapi.Contact(email="contact@yourapi.com"),
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),  # Replace 'accounts.urls' with the actual URL configuration for the 'accounts' app.
    path('api/', include('course.urls')),  # Replace 'course.urls' with the actual URL configuration for the 'course' app.
    path('swagger/', schema_view_accounts.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui-accounts'),
    # path('api/swagger/', schema_view_course.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui-course'),
    
    path('redoc/', schema_view_accounts.with_ui('redoc', cache_timeout=0), name='schema-redoc-ui-accounts'),
    # path('api/redoc/', schema_view_course.with_ui('redoc', cache_timeout=0), name='schema-redoc-ui-course'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

