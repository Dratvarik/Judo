from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Userss
from .forms import UsersForm
from django.core.mail import send_mail

# Create your views here.

def index(request):
    # fs=UsersForm()
    # modell=Userss()
    if request.method == 'POST':
        form = UsersForm(request.POST)
        print(form)
        if form.is_valid(): 
            user=form.save()
        # return HttpResponse('/thanks/')
        # return redirect(user)
        return render(request, 'index.html', )
    else:
        return render(request, 'index.html', )

# def index(request):
#     if request.method == 'POST':
#         form = UsersForm(request.POST)
#         if form.is_valid():
#             subject = "Пробное сообщение"
#             body = {
#                 'surname': form.cleaned_data['surname'],
#                 'name': form.cleaned_data['name'],
#                 'phone': form.cleaned_data['phone'],
#             }
#             message = "\n".join(body.values())
#             send_mail(subject, message, 
#                           'admin@example.com',
#                           ['mmk203@yandex.ru'])
#     return render(request, 'index.html', )


