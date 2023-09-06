from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, AdvertisementForm, ResponseForm
from .models import Advertisement, Response

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            send_verification_email(user)
            return redirect('verification')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def send_verification_email(user):
    # Логика отправки письма с кодом подтверждения регистрации
    pass

def verification(request):
    # Логика подтверждения регистрации
    pass

@login_required
def create_advertisement(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST)
        if form.is_valid():
            advertisement = form.save(commit=False)
            advertisement.user = request.user
            advertisement.save()
            return redirect('advertisement_detail', pk=advertisement.pk)
    else:
        form = AdvertisementForm()
    return render(request, 'create_advertisement.html', {'form': form})

def advertisement_detail(request, pk):
    advertisement = Advertisement.objects.get(pk=pk)
    responses = Response.objects.filter(advertisement=advertisement)
    if request.method == 'POST':
        form = ResponseForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.advertisement = advertisement
            response.user = request.user
            response.save()
            send_response_notification(response)
            return redirect('advertisement_detail', pk=pk)
    else:
        form = ResponseForm()
    return render(request, 'advertisement_detail.html', {'advertisement': advertisement, 'responses': responses, 'form': form})

def send_response_notification(response):
    # Логика отправки уведомления о новом отклике
    pass

@login_required
def private_page(request):
    user = request.user
    advertisements = Advertisement.objects.filter(user=user)
    return render(request, 'private_page.html', {'advertisements': advertisements})

@login_required
def delete_response(request, pk):
    response = Response.objects.get(pk=pk)
    if request.user == response.advertisement.user:
        response.delete()
        return redirect('private_page')

    @login_required
    def accept_response(request, pk):
        response = Response.objects.get(pk=pk)
        if request.user == response.advertisement.user:
            # Логика принятия отклика
            send_acceptance_notification(response)
        return redirect('private_page')

    def send_acceptance_notification(response):
        # Логика отправки уведомления о принятии отклика
        pass