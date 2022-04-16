from django.urls import path


from . import views

urlpatterns = [
    path('', views.horoscope_index, name='horoscope_index'),
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
]