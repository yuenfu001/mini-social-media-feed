from django.urls import path
from post_app import views
from django.contrib.auth.views import LogoutView
# from django.contrib.url
urlpatterns = [
    path("", views.home, name='index'),
    path("my-profile/", views.profile, name='profile'),
    path("view-profile/<int:pk>/", views.check_profile, name='check_profile'),
    path("edit-my-post/<int:post>/", views.edit_post, name='edit_post'),
    path("edit-profile/", views.update_profile, name='edit_profile'),
    path("like-post/<int:liking>/", views.like_tag, name='like_post'),
    path('sign-up/', views.registration,name='register'),
    path('sign-in/',views.CreateLoginView.as_view() ,name='login'),
    path('sign-out/', LogoutView.as_view(), name='logout'),
]
