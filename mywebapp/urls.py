from django.urls import path
from . import views
urlpatterns = [
    path('about/', views.Aboutpage.as_view(), name='about'),
    path('contact/', views.contact, name='contactp'),
    path('', views.ProjectsListView.as_view(), name='projects_list'),
    path('Project/<int:pk>', views.ProjectsDetailView.as_view(),
         name='projects_detail'),
    path('Project/new', views.ProjectsCreateView.as_view(), name='projects_new'),
    path('Project/<int:pk>/edit',
         views.ProjectsUpdateView.as_view(), name='projects_edit'),
    path('Project/<int:pk>/remove/', views.ProjectsDeleteView.as_view(),
         name='projects_remove'),
    # Certificates
    path('my/', views.CertificatesListView.as_view(), name='certificates_list'),
    path('my/certificates/<int:pk>', views.CertificatesDetailView.as_view(),
         name='certificates_detail'),
    path('my/certificates/new', views.CertificatesCreateView.as_view(),
         name='certificates_new'),
    path('my/certificates/<int:pk>/edit',
         views.CertificatesUpdateView.as_view(), name='certificates_edit'),
    path('my/certificates/<int:pk>/remove/', views.CertificatesDeleteView.as_view(),
         name='certificates_remove'),
]
