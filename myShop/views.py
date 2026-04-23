from django.views.generic import ListView, DetailView, TemplateView, FormView
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from .models import Category, Product
from .forms import RegisterForm, LoginForm


class CategoriesView(ListView):
    model = Category
    template_name = "categories.html"
    context_object_name = "categories"


class ProductsView(ListView):
    model = Product
    template_name = "products.html"
    context_object_name = "products"


class CategoryProductsView(DetailView):
    model = Category
    template_name = "category_products.html"
    pk_url_kwarg = "id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.filter(category=self.object)
        return context


class ShopHomeView(TemplateView):
    template_name = "shop_home.html"


class RegisterView(FormView):
    template_name = "register.html"
    form_class = RegisterForm

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return redirect('login')


class LoginView(FormView):
    template_name = "login.html"
    form_class = LoginForm

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(self.request, username=username, password=password)

        if user:
            login(self.request, user)
            return redirect('home')

        return self.form_invalid(form)