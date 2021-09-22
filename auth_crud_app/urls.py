from django.urls import path
from .views import user_signup_view, user_login_view, indexView, user_logout,addStudent_view,aboutView,contactView,deleteStudentView, updateStudentView,activate

urlpatterns = [
    path('', user_signup_view, name='signUp'),
    path('login/', user_login_view, name='login'),
    path('activate/<uidb64>/<token>/',activate , name='activate'),
    path('logout/', user_logout, name='logout'),
    path('index/', indexView, name='index'),
    path('addstudent/', addStudent_view, name='addstudent'),
    path('update/<int:id>/', updateStudentView, name='update'),
    path('delete/<int:id>/', deleteStudentView, name='delete'),
    path('about/', aboutView, name='about'),
    path('contact/', contactView, name='contact'),

]
