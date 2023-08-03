from django.urls import path

from appname import views

app_name= 'appname'
urlpatterns = [

    path('about.html', views.about, name = "about.html"),
    path('contact.html', views.contact, name = "contact.html"),
    path('index.html', views.index, name = "index.html"),
    path('portfolio-details.html', views.portfoliodetails, name = "portfolio-details.html"),
    path('portfolio.html', views.portfolio, name = "portfolio.html"),
    path('resume.html', views.resume, name = "resume.html"),
    path('services.html', views.services, name = "services.html"),

    ### for user registratio, sign-in sign-out
    path('base', views.base, name = 'base'),
    path('register', views.register, name = 'register'),
    path('login_reg', views.login_reg, name = 'login_reg'),
    path('logout', views.logoutuser, name = 'logout'),

]
