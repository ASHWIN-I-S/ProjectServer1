from django.urls import path, include
from app import views

urlpatterns = [

path('index/', views.index, name = 'index'),
path('about/', views.about, name = 'about'),
path('blog/', views.blog, name = 'blog'),
path('contact/', views.contact, name = 'contact'),
path('FAQ/', views.FAQ, name = 'FAQ'),
path('404/', views._404, name = '404'),
path('feature/', views.feature, name = 'feature'),
path('offer/', views.offer, name = 'offer'),
path('team/', views.team, name = 'team'),
path('service/', views.service, name = 'service'),
path('testimonial/', views.testimonial, name = 'testimonial'),
]