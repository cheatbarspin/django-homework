from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'main/home.html')


def index2(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'You have new message from {name}({phone}): {message}')
    return render(request, 'main/contacts.html')
