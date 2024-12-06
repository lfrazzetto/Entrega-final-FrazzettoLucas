from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib import messages

# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


# Creo vista para mostrar el perfil
@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html', {'user': request.user})


# Creo vista para editar el perfil
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES,
                           instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Perfil actualizado correctamente!")
            return redirect('profile')
        else:
            messages.error(
                request, "Hubo un error al actualizar el perfil. Revisa los campos.")
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'accounts/edit_profile.html', {'form': form})

# Creo vista para eliminar una cuenta


@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        logout(request)  # Cierra la sesión antes de eliminar la cuenta
        user.delete()  # Elimina el usuario y su perfil asociado
        messages.success(request, "Tu cuenta ha sido eliminada exitosamente.")
        return redirect('home')  # Redirige a la página principal
    return render(request, 'accounts/delete_account.html')
