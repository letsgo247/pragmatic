from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

# from accountapp.views import hello_world
from accountapp.views import AccountDetailView, hello_world, AccountCreateView

app_name = "accountapp"


urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'), # login&logout view는 따로 view 생성 없이 기존 제공되는 걸 사용하기 땜에 template을 여기서 넣어주는 것임!!!
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', AccountCreateView.as_view(), name='create'),
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail')
]