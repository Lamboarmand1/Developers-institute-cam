from django.shortcuts import render, redirect
from .forms import Register_form, UserForm


# Create your views here.
from .models import Profile


def register(request):

    if request.method == 'POST':
        print('in post method')
        r_form = Register_form(request.POST, request.FILES)
        u_form = UserForm(request.POST)
        if r_form.is_valid() and u_form.is_valid() :
            print('in valid')
            image = r_form.cleaned_data.get('image')
            bio = r_form.cleaned_data.get('bio')
            new_user = u_form.save()
            new_profile= Profile(profile_image=image, bio=bio, user=new_user)
            new_profile.save()
            print('profile created')
            return redirect('home')
    else:
        r_form = Register_form()
        u_form = UserForm()
    return render(request, 'register.html', {'form1': r_form,
                                      'form2': u_form})
