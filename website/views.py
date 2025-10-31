from django.shortcuts import render

# Create your views here.

def home(request):

    return render(request,'website/home.html')


def product(request):
    return render(request,'website/product.html')

def about(request):
    return render(request, 'website/about.html')

def contact(request):
    if request.method == 'POST':
        # Handle form submission
        # Send email, save to database, etc.
        pass
    return render(request, 'website/contact.html')