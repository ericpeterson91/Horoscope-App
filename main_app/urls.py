from django.urls import path, include


from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/profile/', views.profile, name="profile"), #change here from 'profiles/'
    # path('profile/', views.profile, name="profile"),
    path('profile/', views.profile, name="profile"),
    # path('accounts/profile/', views.profile, name="profile"), #change here from 'profiles/'
    path('edit/', views.edit, name="edit"),
    path('edit_after/', views.edit_after, name="edit_after"),
    path('profile/', views.profile, name="profile"),
    path('matches/', views.matches, name="matches"),
    path('profile/new', views.ProfileCreate.as_view(), name='profile_create'),
    path('profile/<int:pk>/delete/', views.ProfileDelete.as_view(), name='profile_delete'),
    path('profile/<int:pk>/update/', views.ProfileUpdate.as_view(), name='profile_update'),
    # path('accounts/', views.login, name="login"),
    path('accounts/signup/', views.signup, name="signup"),
    path('intro_one/', views.intro_one, name="intro_one"),
    path('intro_two/', views.intro_two, name="intro_two"),
    path('intro_three/', views.intro_three, name="intro_three"),
    path('questions_one/', views.questions_one, name="questions_one"),
    path('questions_two/', views.questions_two, name="questions_two"),
    path('questions_three/', views.questions_three, name="questions_three"),
    path('questions_matches/', views.questions_matches, name="questions_matches"),
    path('horoscope/', views.horoscope, name="horoscope"),



    path('add_photo/', views.add_photo, name='add_photo'),
    path('accounts/', include('django.contrib.auth.urls'))
    # path('accounts/', include('django.contrib.auth.urls'))
]