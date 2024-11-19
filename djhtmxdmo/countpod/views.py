from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def index(request):
    print("index A")
    return render(request, "countpod/index.html", {})

def countup(request):
    print("countup A")
    return HttpResponseRedirect(reverse("countpod:index")) 

def countdown(request):
    print("countdown A")
    return HttpResponseRedirect(reverse("countpod:index")) 

def count(request):
    print("count A")
    import pdb;pdb.set_trace()
    if request.method == 'POST':
        action = request.POST.get('action')  # Get the action value from the button

        if action == 'increment':
            print("countup B")

        elif action == 'decrement':
            print("countdown B")

    return HttpResponseRedirect(reverse("countpod:index")) 

'''
def your_view(request):
    print("your_view G")
    context = {
        'data': 'Initial data',  # Replace with actual initial data
    }
    print("your_view H")

    if request.method == 'POST':
        action = request.POST.get('action')  # Get the action value from the button

        if action == 'process_one':
            print("your_view X")
            # Perform processing for the first button
            processed_data = 'Data updated by Processing 1'
            context['data'] = processed_data

        elif action == 'process_two':
            print("your_view Z")
            # Perform processing for the second button
            processed_data = 'Data updated by Processing 2'
            context['data'] = processed_data

    return render(request, "countpod/index.html", context)

'''
