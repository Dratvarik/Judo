from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Userss
from .forms import UsersForm

# Create your views here.

def index(request):
    # fs=UsersForm()
    # modell=Userss()
    if request.method == 'POST':
        form = UsersForm(request.POST)
        print(form)
        if form.is_valid(): 
            user=form.save()
            # return HttpResponseRedirect('/thanks/')
            # return redirect(user)
        return render(request, 'index.html', )
    else:
        return render(request, 'index.html', )


# def register(request):
#     register_form = RegistrationForm()
#     if request.method=='POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             new_user = User.objects.create_user(username=request.POST['username'], 
#                                             email=request.POST['email'], 
#                                             password=request.POST['password1'])
#             new_user.is_active = False
#             new_user.save()
#             return HttpResponseRedirect(reverse('index'))
#     return render_to_response('registration/registration_form.html'{'form':register_form})
# # def addusers(request):
   
    

# def get_name(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = Userss(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('/thanks/')

#     # # if a GET (or any other method) we'll create a blank form
#     # else:
#         form = Userss()

#     return render(request, 'name.html', {'form': form})