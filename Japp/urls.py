from django.urls import path
from Japp import views
from AJShop import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home',views.home),
    path('aboutus',views.aboutus),
    path('pdetails/<pid>',views.pdetails),
    path('viewcart',views.viewcart),
    path('register',views.register),
    path('login',views.ulogin),
    path('logout',views.ulogout),
    path('catfilter/<cv>',views.catfilter),
    path('range',views.range),
    path('addtocart/<pid>',views.addtocart),
    path('remove/<cid>',views.remove),
    path('updateqty/<qv>/<cid>',views.updateqty),
    path('placeorder',views.placeorder),
    path('makepayment',views.makepayment),
    path('sendmail',views.sendusermail),
    path('pfilter/<pv>',views.Pfilter),
    path('oremove/<cid>',views.oremove),
]  


#if settings.DEBUG: 
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)