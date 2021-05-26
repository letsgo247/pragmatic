from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from accountapp.models import HelloWorld


def hello_world(request):
    if request.method == 'POST':

        temp = request.POST.get('hello_world_input')
        post = request.POST
        new_hello_world = HelloWorld()
        print(new_hello_world)
        new_hello_world.text = temp
        print(new_hello_world)
        new_hello_world.save()
        print(new_hello_world)
        print(new_hello_world.text)

        return render(request, 'accountapp/hello_world.html', context={'hello_world_output': new_hello_world, 'post':post})

    else:
        return render(request, 'accountapp/hello_world.html', context={'text': 'GET METHOD?'})
