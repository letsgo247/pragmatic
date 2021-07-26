from accountapp.forms import AccountUpdateForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import DeleteView, UpdateView

# Create your views here.
from accountapp.models import HelloWorld

from django.views.generic import CreateView, DetailView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


def hello_world(request):
    if request.method == 'POST':
        temp = request.POST.get('hello_world_input')
        post = request.POST

        new_hello_world = HelloWorld()  # DB 클래스의 인스턴스?
        print('1)', new_hello_world)
        new_hello_world.text = temp     # post 내용 db에 집어넣기
        print('2)', new_hello_world)
        new_hello_world.save()
        print('3)', new_hello_world)

        hello_world_list = HelloWorld.objects.all()

        # print(reverse('test'))

        # return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list, 'post':post})
        # return HttpResponseRedirect('/account/hello_world')
        return HttpResponseRedirect(reverse('accountapp:hello_world'))



    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})



 
class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

    
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'


class AccountDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'