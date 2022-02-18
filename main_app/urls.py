from django.urls import path, include


from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name="profile"),
    path('horoscope/', views.horoscope, name="horoscope"),
    path('profile/<int:pk>', views.profile_view, name="profile_view"),
    path('matches/', views.matches, name="matches"),
    path('profile/new/', views.ProfileCreate.as_view(), name='profile_create'),
    path('horoscope/new/', views.HoroscopeCreate.as_view(), name='horoscope_create'),
    path('profile/<int:pk>/delete/', views.ProfileDelete.as_view(), name='profile_delete'),
    path('profile/<int:pk>/update/', views.ProfileUpdate.as_view(), name='profile_update'),
    path('horoscope/<int:pk>/update/', views.HoroscopeUpdate.as_view(), name='horoscope_update'), 
    path('accounts/signup/', views.signup, name="signup"),
    path('intro_one/', views.intro_one, name="intro_one"),
    path('intro_two/', views.intro_two, name="intro_two"),
    path('intro_three/', views.intro_three, name="intro_three"),
    path('questions_two/', views.questions_two, name="questions_two"),
    path('questions_three/', views.questions_three, name="questions_three"),
    path('questions_matches/', views.questions_matches, name="questions_matches"),

    path('horoscope_index/', views.horoscope_index, name="horoscope_index"),
    path('aries/', views.aries, name="aries"),
    path('taurus/', views.taurus, name="taurus"),
    path('gemini/', views.gemini, name="gemini"),
    path('cancer/', views.cancer, name="cancer"),
    path('leo/', views.leo, name="leo"),
    path('virgo/', views.virgo, name="virgo"),
    path('libra/', views.libra, name="libra"),
    path('scorpio/', views.scorpio, name="scorpio"),
    path('sagitarius/', views.sagitarius, name="sagitarius"),
    path('capricorn/', views.capricorn, name="capricorn"),
    path('aquarius/', views.aquarius, name="aquarius"),
    path('pisces/', views.pisces, name="pisces"),


    path('accounts/', include('django.contrib.auth.urls'))
]