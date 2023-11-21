from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views


urlpatterns = [
				path('',views.Home,name="Home"),
				path('User_Login/',views.User_Login,name='User_Login'),
				path('Admin_Login/',views.Admin_Login,name='Admin_Login'),
				path('User_Registration/',views.User_Registration,name='User_Registration'),
				path('View_User/',views.View_User,name='View_User'),
				path('Profile/',views.Profile,name='Profile'),
				path('Answer/',views.Answer,name='Answer'),
				path('View_Query/',views.View_Query,name='View_Query'),
				path('Ask_Help/',views.Ask_Help,name='Ask_Help'),
				path('Add_Information/',views.Add_Information,name='Add_Information'),
				path('Calculator/',views.Calculator,name='Calculator'),
				path('View_Information/',views.View_Information,name='View_Information'),
				path('Dashboard/',views.Dashboard,name='Dashboard'),
				path('ViewUser_Query/',views.ViewUser_Query,name='ViewUser_Query'),
				path('Logout/',views.Logout,name="Logout"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)