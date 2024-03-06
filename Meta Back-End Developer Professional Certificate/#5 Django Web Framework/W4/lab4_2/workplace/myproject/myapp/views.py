from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu  # Assuming you've already imported this from Step 3

def menu(request):
    # Fetch all menu items from the database
    menu_items = Menu.objects.all()

    # Create a dictionary to pass as context to the template
    items_dict = {'menu': menu_items}

    # Use the render function to render the menu.html template with the items_dict
    return render(request, 'menu.html', items_dict)
