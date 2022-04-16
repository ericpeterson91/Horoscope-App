from django.shortcuts import render


def horoscope_index(request):
    return render(request, 'horoscopes/horoscope_index.html')

def aries(request):
    return render(request, 'horoscopes/aries.html')

def taurus(request):
    return render(request, 'horoscopes/taurus.html')

def gemini(request):
    return render(request, 'horoscopes/gemini.html')

def cancer(request):
    return render(request, 'horoscopes/cancer.html')

def leo(request):
    return render(request, 'horoscopes/leo.html')

def virgo(request):
    return render(request, 'horoscopes/virgo.html')

def libra(request):
    return render(request, 'horoscopes/libra.html')

def scorpio(request):
    return render(request, 'horoscopes/scorpio.html')

def sagitarius(request):
    return render(request, 'horoscopes/sagitarius.html')

def capricorn(request):
    return render(request, 'horoscopes/capricorn.html')

def aquarius(request):
    return render(request, 'horoscopes/aquarius.html')

def pisces(request):
    return render(request, 'horoscopes/pisces.html')

