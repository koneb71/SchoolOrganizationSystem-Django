from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.contrib.auth import authenticate, login, logout
from app.models import User


def user_login(request):
    if request.method == 'POST':

        try:
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return redirect('app.views.user_home')
            else:
                log_fail = True
                return render(request, 'app/login.html', {'log_fail': log_fail})

        except User.DoesNotExist:
            return redirect('app.views.user_login')

    elif request.user.is_authenticated():
        return redirect('app.views.user_home')

def user_logout(request):
    logout(request)
    return redirect('app.views.user_home')


def password_change(request):
    form = ChangePasswordForm(request.POST)
    if request.method == "POST" and form.is_valid():
        new_pass = form.cleaned_data['password']
        confirm_pass = form.cleaned_data['confirm_password']
        if new_pass == confirm_pass:
            request.user.set_password(form.cleaned_data['password'])
            request.user.save()
            return redirect('app.views.succ_pass')
        else:
            pass_fail = True
            return render(request, 'app/changepassword.html', {'pass_fail': pass_fail})
    else:
        form = ChangePasswordForm()
    return render(request, 'app/changepassword.html', {'form': form})


    return render(request, 'app/login.html')