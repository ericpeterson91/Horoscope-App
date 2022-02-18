from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile, Horoscope
from django.contrib.auth.models import User
from django.db.models import Q

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('/profile/new')
    else:
      error_message = 'Invalid credentials - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


@login_required
def profile_view(request, pk):
    profile = Profile.objects.get(user__pk = pk)
    return render(request, 'accounts/profile_view.html', { 'profile': profile, 'user': request.user })


@login_required
def matches(request):
    user_sign = request.user.horoscope.horoscope
    print(user_sign)
    if user_sign == 'VI' or user_sign == 'PI':
        matches = User.objects.filter(
            Q(horoscope__horoscope = 'CP') | Q(horoscope__horoscope = 'CA') | Q(horoscope__horoscope = 'TA') | Q(horoscope__horoscope = 'SC'))[:3]
        print(matches)
        return render(request, 'matches.html', { 'matches': matches, 'user': request.user })
    if user_sign == 'AR' or user_sign == 'LI':
        matches = User.objects.filter(
            Q(horoscope__horoscope = 'GE') | Q(horoscope__horoscope = 'LE') | Q(horoscope__horoscope = 'SA') | Q(horoscope__horoscope = 'AQ'))[:3]
        print(matches)
        return render(request, 'matches.html', { 'matches': matches, 'user': request.user })
    if user_sign == 'TA' or user_sign == 'SC':
        matches = User.objects.filter(
            Q(horoscope__horoscope = 'CA') | Q(horoscope__horoscope = 'VI') | Q(horoscope__horoscope = 'CP') | Q(horoscope__horoscope = 'PI'))[:3]
        print(matches)
        return render(request, 'matches.html', { 'matches': matches, 'user': request.user })
    if user_sign == 'GE' or user_sign == 'SA':
        matches = User.objects.filter(
            Q(horoscope__horoscope = 'LI') | Q(horoscope__horoscope = 'AQ') | Q(horoscope__horoscope = 'AR') | Q(horoscope__horoscope = 'LE'))[:3]
        print(matches)
        return render(request, 'matches.html', { 'matches': matches, 'user': request.user })
    if user_sign == 'CA' or user_sign == 'CP':
        matches = User.objects.filter(
            Q(horoscope__horoscope = 'TA') | Q(horoscope__horoscope = 'VI') | Q(horoscope__horoscope = 'SC') | Q(horoscope__horoscope = 'PI'))[:3]
        print(matches)
        return render(request, 'matches.html', { 'matches': matches, 'user': request.user })
    if user_sign == 'LE' or user_sign == 'AQ':
        matches = User.objects.filter(
            Q(horoscope__horoscope = 'AR') | Q(horoscope__horoscope = 'GE') | Q(horoscope__horoscope = 'LI') | Q(horoscope__horoscope = 'SA'))[:3]
        print(matches)
        return render(request, 'matches.html', { 'matches': matches, 'user': request.user })


class ProfileCreate(LoginRequiredMixin, CreateView):
    model = Profile
    fields = ['first_name', 'last_name', 'instagram_url']
    success_url = '/horoscope/new'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class HoroscopeCreate(LoginRequiredMixin, CreateView):
    model = Horoscope
    fields = ['horoscope']
    success_url = '/profile/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class HoroscopeUpdate(LoginRequiredMixin, UpdateView):
    model = Horoscope
    fields = ['horoscope']
    success_url = '/profile/'

class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ['first_name', 'last_name', 'instagram_url']
    success_url = '/profile/'

class ProfileDelete(DeleteView):
  model = Profile
  success_url = '/profile/new'


#-----------------------------------------------------------------------------------------------------------------------------------



def home(request):
    return render(request, 'home.html')


@login_required
def profile(request):
    profile = Profile.objects.get(user = request.user)
    return render(request, 'profile.html', {
        "profile": profile
    })

@login_required
def edit(request):
    profile = Profile.objects.get(user = request.user)
    return render(request, 'edit.html', {
        "profile": profile
    })

@login_required
def edit_after(request):
    profile = Profile.objects.get(user = request.user)
    return render(request, 'edit_after.html', {
        "profile": profile
    }
    )

@login_required
def horoscope(request):
    profile = Profile.objects.get(user = request.user)
    return render(request, 'horoscope.html', {
        "profile": profile
    })

def matches(request):
    return render(request, 'matches.html')

def intro_one(request):
    return render(request, 'intro/intro_one.html')

def intro_two(request):
    return render(request, 'intro/intro_two.html')

def intro_three(request):
    return render(request, 'intro/intro_three.html')

def questions_one(request):
    return render(request, 'questions/questions_one.html')

def questions_two(request):
    return render(request, 'questions/questions_two.html')

def questions_three(request):
    return render(request, 'questions/questions_three.html')

def questions_matches(request):
    return render(request, 'questions/questions_matches.html')




# @login_required
# def add_photo(request, profile_id):
#     photo_file = request.FILES.get('photo-file', None)
#     if photo_file:
#         s3 = boto3.client('s3')
#         key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
#         try:
#           s3.upload_fileobj(photo_file, BUCKET, key)
#           url = f"{S3_BASE_URL}{BUCKET}/{key}"
#           photo = Photo(url=url, character_id=profile_id)
#           photo.save()
#         except:
#             print('An error occurred uploading file to S3')
#     return redirect('detail', character_id=character_id)


# ask where this is from 

# def signup(request):
#   error_message = ''
#   if request.method == 'POST':
#     # This is how to create a 'user' form object
#     # that includes the data from the browser
#     form = UserCreationForm(request.POST)
#     if form.is_valid():
#       # This will add the user to the database
#       form.save() #change from user=form.save
#       # This is how we log a user in via code
#       login(request)
#       return redirect('profile/')
#     else:
#       error_message = 'Invalid sign up - try again'
#   # A bad POST or a GET request, so render signup.html with an empty form
#   form = UserCreationForm()
#   context = {'form': form, 'error_message': error_message}
#   return render(request, 'registration/signup.html', context)
