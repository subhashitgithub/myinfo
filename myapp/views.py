from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    
    return render(request, 'services.html')



def contact(request):
    return render(request, 'contact.html')


def handleSignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        print(username, pass1, pass2)
        
    if pass1 != pass2:
        messages.error(request, "password do not match")
    else:
        myuser = User.objects.create_user(username, email, pass1)
        
        myuser.save()

        messages.success(request, "Your Account created successful")
    return redirect('/')