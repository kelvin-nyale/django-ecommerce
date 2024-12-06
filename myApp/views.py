from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from myApp.models import Users, Products, Services, Categories
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
# from datetime import datetime




# Create your views here.
def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        user_role = request.POST.get('user_role')
        date_registered = request.POST.get('date_registered')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if user with this email already exists
        if Users.objects.filter(email=email).exists():
            messages.error(request, "User with this email already exists")
            return redirect('register')

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        # Create new user
        user = Users.objects.create(
            user_name=user_name,
            email=email,
            phone=phone,
            user_role=user_role,
            date_registered=date_registered,
            password=make_password(password)
        )
        user.save()

        messages.success(request, "Registration successful! You can now log in.")
        return redirect('login')

    return render(request, 'register.html')

# def login(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#
#         try:
#             # Retrieve the user by email
#             user = Users.objects.get(email=email)
#
#             # Verify the password
#             if user.check_password(password):
#                 # Authentication successful, redirect based on user role
#                 request.session['user_id'] = user.id  # Store user ID in session
#                 messages.success(request, f"Welcome back, {user.user_name}!")
#
#                 if user.user_role == 'admin':
#                     return redirect('admin_dashboard')
#                 elif user.user_role == 'seller':
#                     return redirect('seller_dashboard')
#                 elif user.user_role == 'user':
#                     return redirect('user_dashboard')
#                 else:
#                     return redirect('user_dashboard')  # Default fallback
#             else:
#                 messages.error(request, "Invalid password.")
#         except Users.DoesNotExist:
#             messages.error(request, "User with this email does not exist.")
#
#         return redirect('login')  # Redirect back to login page on failure
#
#     return render(request, 'login.html')  # Render the login page

User = get_user_model()
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        print(f'{email} {password}')
        # Validate email and password input
        if not email or not password:
            messages.error(request, "Both email and password are required.")
            return redirect('login')
        print(">>>>>>>>>>>>Email and password validation complete")
        # Authenticate the user
        user = authenticate(request, email=email, password=password)
        print(user)
        if user is not None:
            print(">>>>>Trying to log user")
            login(request, user)  # Log the user in
            print(">>>>>>>Checking role for redirections")
            # Redirect based on user role
            if hasattr(user, 'user_role'):
                if user.user_role == 'admin':
                    messages.success(request, "Welcome back, Admin!")
                    return redirect('admin_dashboard')
                elif user.user_role == 'seller':
                    messages.success(request, "Welcome back, Seller!")
                    return redirect('seller_dashboard')
                elif user.user_role == 'user':
                    print("user role hit======awaiting redirect")
                    messages.success(request, "Welcome back, User!")
                    print(">>>>>redirect reached")
                    return redirect('user_dashboard')

            # Default fallback if no specific role logic is set
            messages.success(request, "Login successful!")
            return redirect('user_dashboard')
        else:
            messages.error(request, "Invalid email or password.")
            return redirect('login')

    return render(request, 'login.html')

# User = get_user_model()


# def login(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#
#         # Validate email and password input
#         if not email or not password:
#             messages.error(request, "Both email and password are required.")
#             return redirect('login')
#
#         # Fetch user by email
#         try:
#             user = Users.objects.get(username=email)
#         except Users.DoesNotExist:
#             messages.error(request, "Invalid email or password.")
#             return redirect('login')
#
#         # Check password
#         if user.password == password:  # For plaintext passwords (not recommended)
#             auth_login(request, user)
#             return redirect('user_dashboard')
#
#         # If using hashed passwords
#         if user.check_password(password):
#             auth_login(request, user)
#             return redirect('user_dashboard')
#
#         messages.error(request, "Invalid email or password.")
#         return redirect('login')
#
#     return render(request, 'login.html')

# # ADMIN OPERATIONS AND PRIVILEGES
@login_required
def dashboard(request):
    return render(request, 'admin_dashboard.html')

# # USERS CRUD OPERATIONS
@login_required
def add_user(request):
    if request.method == 'POST':
        user_name=request.POST.get('user_name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        Users.objects.create(user_name=user_name, email=email, phone=phone, password=password)
        return redirect('users')
    return render(request, 'add_user.html')
#
@login_required
def users(request):
    users=Users.objects.all()
    return render(request, 'users.html', {'users':users})

@login_required
def update_user(request,pk):
    user=get_object_or_404(Users, pk=pk)
    # user=Users.objects.get(Users,pk=id)
    if request.method == 'POST':
        user.user_name=request.POST.get('user_name')
        user.email=request.POST.get('email')
        user.phone=request.POST.get('phone')
        user.password=request.POST.get('password')
        user.save()
        return redirect('users')
    return render(request, 'update_user.html', {'user':user})

@login_required
def delete_user(request,pk):
    user=get_object_or_404(Users, pk=pk)
    # user=Users.objects.get(Users,pk=id)
    if request.method == 'POST':
        user.delete()
        return redirect('users')
    return render(request, 'delete_user.html', {'user':user})
#
# # PRODUCTS CRUD OPERATIONS
@login_required
def add_product(request):
    if request.method == 'POST':
        product_id=request.POST.get('product_id')
        product_name=request.POST.get('product_name')
        description = request.POST.get('description')
        price=request.POST.get('price')
        Products.objects.create(product_id=product_id, product_name=product_name, description=description, price=price)
        return redirect('products')
    return render(request, 'add_product.html')

@login_required
def products(request):
    products=Products.objects.all()
    return render(request, 'products.html', {'products':products})
#
@login_required
def update_product(request,pk):
    product=get_object_or_404(Products, pk=pk)
    # product=Products.objects.get(Products,pk=id)
    if request.method == 'POST':
        product.product_id=request.POST.get('product_id')
        product.product_name=request.POST.get('product_name')
        product.description=request.POST.get('description')
        product.price=request.POST.get('price')
        product.save()
        return redirect('products')
    return render(request, 'update_product.html', {'product':product})
#
@login_required
def delete_product(request):
    product=get_object_or_404(Products, pk=id)
    # product=Products.objects.get(Products,pk=id)
    if request.method == 'POST':
        product.delete()
        return redirect('products')
    return render(request, 'delete_product.html',{'product':product})

# # SERVICES CRUD OPERATIONS
@login_required
def add_service(request):
    if request.method == 'POST':
        service_name=request.POST.get('service_name')
        description=request.POST.get('description')
        price=request.POST.get('price')
        Services.objects.create(service_name=service_name, description=description, price=price)
        return redirect('services')
    return render(request, 'add_service.html')

@login_required
def services(request):
    services=Services.objects.all()
    return render(request, 'services.html', {'services':services})

@login_required
def update_service(request,pk):
    service=get_object_or_404(Services, pk=pk)
    # service=Services.objects.get(Services,pk=id)
    if request.method == 'POST':
        service.service_name=request.POST.get('service_name')
        service.description=request.POST.get('description')
        service.price=request.POST.get('price')
        service.save()
        return redirect('services')
    return render(request, 'update_service.html', {'service':service})

@login_required
def delete_service(request):
    service=get_object_or_404(Services, pk=id)
    # service=Services.objects.get(Services,pk=id)
    if request.method == 'POST':
        service.delete()
        return redirect('services')
    return render(request, 'delete_service.html', {'service':service})

# CATEGORIES CRUD OPERATIONS
@login_required
def add_category(request):
    if request.method == 'POST':
        category_id=request.POST.get('category_id')
        category_name=request.POST.get('service_name')
        description=request.POST.get('description')
        Categories.objects.create(category_id=category_id, category_name=category_name, description=description)
        return redirect('services')

    return render(request, 'add_category.html')

@login_required
def categories(request):
    categories=Categories.objects.all()
    return render(request, 'categories.html', {'categories':categories})

@login_required
def update_category(request,pk):
    category=get_object_or_404(Categories,pk=pk)
    # category=Categories.objects.get(Categories,pk=id)
    if request.method == 'POST':
        category.category_id=request.POST.get('category_id')
        category.category_name=request.POST.get('category_name')
        category.description=request.POST.get('description')
        category.save()
        return redirect('categories')

    return render(request, 'update_category.html', {'category':category})

@login_required
def delete_category(request):
    category=get_object_or_404(Categories,pk=id)
    # category=Categories.objects.get(Categories,pk=id)
    if request.method == 'POST':
        category.delete()
        return redirect('categories')
    return render(request, 'delete_category.html')

@login_required
def seller_dashboard(request):
    return render(request, 'seller_dashboard.html')

@login_required
def upload_product(request):
    return render(request, 'seller.upload_products.html')

# CART OPERATIONS
@login_required
def add_to_cart(request):
    return render(request,'add_to_cart.html')

@login_required
def cart_items(request):
    return render(request, 'cart.html')

@login_required
def delete_from_cart(request):
    return render(request,'delete_from_cart.html')

@login_required
def user_dashboard(request):
    return render(request, 'user_dashboard.html')
#
@login_required
def logout(request):
    return render(request,'logout.html')