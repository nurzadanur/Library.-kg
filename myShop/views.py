from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login


def categories_view(request):
    categories = Category.objects.all()
    return render(request, "categories.html", {"categories": categories})


def products_view(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


def category_products_view(request, id):
    category = get_object_or_404(Category, id=id)
    products = Product.objects.filter(category=category)

    return render(request, "category_products.html", {
        "category": category,
        "products": products
    })

def shop_home(request):
    return render(request, "shop_home.html")


def register(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')

    return render(request, "register.html", {"form": form})




def login_view(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return redirect('home')

    return render(request, "login.html", {"form": form})