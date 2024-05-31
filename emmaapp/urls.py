from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static


router = DefaultRouter()
router.register(r'candidates', views.CandidateViewSet)

urlpatterns = [
    path('', views.candidate_list, name='candidate_list'),
    path('candidate/<int:candidate_id>/', views.candidate_detail, name='candidate_detail'),
    path('candidate/new/', views.candidate_create, name='candidate_create'),
    path('candidate/<int:candidate_id>/edit/', views.candidate_update, name='candidate_update'),
    path('candidate/<int:candidate_id>/delete/', views.candidate_delete, name='candidate_delete'),
    path('api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

