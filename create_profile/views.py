
from django.shortcuts import render
from .forms import admitCardForm
from .models import admit_card
from django.conf import settings
from django.http.response import HttpResponseRedirect
from django.urls import reverse

import cv2

def fd(path):
     # Load the cascade
    face_cascade = cv2.CascadeClassifier('media/xml_file/haarcascade_frontalface_default.xml')
    # Read the input image
    img = cv2.imread(f'media/{path}')
    #img = cv2.imread(f'static/imgfolder/{path}')
    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    type_of_data = type(faces)

    if str(type_of_data) == "<class 'numpy.ndarray'>":
        return 1
    else:
        return 0

def create_profile(request):
    form = admitCardForm()
    if request.method == 'POST':
        form = admitCardForm(request.POST, request.FILES)
        if form.is_valid():
           ins = form.save()
           print(ins.email)
           return HttpResponseRedirect(reverse('create_profile:show_card', args=[ins.email]))
        else:
            print(form.errors)
    context = {'form': form}
    return render(request, 'create_profile/index.html', context)


def show_card(request, pk):
    data = admit_card.objects.get(email=pk)
    personalPhoto=data.profile_image
    profile_image = ""
    sign_image = ""
    if fd(str(personalPhoto)) == 0:
        profile_image = data.sign_image.url
        sign_image = data.profile_image.url
    elif fd(str(personalPhoto)) == 1:
        profile_image = data.profile_image.url
        sign_image = data.sign_image.url
    context = {'data': data, 'profile_image': profile_image, 'sign_image': sign_image}
    return render(request, 'create_profile/show_card.html', context)

def card_temp(request):
    return render(request, 'create_profile/card_temp.html')