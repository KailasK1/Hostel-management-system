from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User, Room
from .forms import RoomForm
from .forms import UserForm  # You'll need a form to add the user (you can create this)
from django.contrib import messages


# Home Page View
def home(request):
    return render(request, 'home.html')


# Admin Login View
def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Fixed username and password for admin
        if username == 'admin' and password == 'admin123':
            # Redirect to admin dashboard
            return redirect('admin_dashboard')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'admin_login.html')


# Admin Dashboard View
def admin_dashboard(request):
    # Retrieve all rooms and users for display
    rooms = Room.objects.all()
    users = User.objects.all()
    return render(request, 'admin_dashboard.html', {'rooms': rooms, 'users': users})


# User Login View
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        login_key = username + "123"  # Generate the expected login key (username + 123)

        if not username:
            messages.error(request, 'Please enter a username.')
            return render(request, 'user_login.html')  # Return the form with error

        # Check if the username matches a user and the login_key
        try:
            user = User.objects.get(name=username)
            if user.login_key == login_key:  # Check if the login key is correct
                messages.success(request, f'Welcome back, {user.name}!')
                return redirect('user_dashboard', user_id=user.id)
            else:
                messages.error(request, 'Invalid login key (username + 123).')
        except User.DoesNotExist:
            messages.error(request, 'User with this username does not exist.')

    return render(request, 'user_login.html')



# User Dashboard View
def user_dashboard(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        return render(request, 'user_dashboard.html', {'user': user})
    except User.DoesNotExist:
        messages.error(request, 'User does not exist')
        return redirect('user_login')

def add_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin-dashboard')  # Redirect back to the admin dashboard
    else:
        form = RoomForm()

    return render(request, 'add_room.html', {'form': form})

def add_user_to_room(request, room_id):
    # Get the room object using the provided room_id
    room = Room.objects.get(id=room_id)

    # Check if the room is available
    if room.is_vacant:
        if request.method == 'POST':
            # Assign the room to the user
            form = UserForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.room = room  # Assign the room to the user
                user.save()
                room.is_vacant = False  # Mark the room as not vacant
                room.save()
                return redirect('admin-dashboard')  # Redirect back to the admin dashboard
        else:
            form = UserForm()

        return render(request, 'add_user_to_room.html', {'form': form, 'room': room})

    else:
        return redirect('admin-dashboard')


def some_view(request):
    # after some logic, redirect to the admin dashboard
    return redirect('admin-dashboard')

def vacate_room(request, room_id):
    # Logic to vacate the room (mark as available, etc.)
    room = Room.objects.get(id=room_id)
    room.is_available = True  # or whatever logic you want to use
    room.save()

    # After vacating the room, redirect somewhere (e.g., back to the dashboard)
    return redirect('admin-dashboard')

def some_view(request, room_id):
    # After some logic, redirect to vacate the room
    return redirect('vacate_room', room_id=room_id)