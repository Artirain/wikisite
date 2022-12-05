from django.urls import path
from .views import *



#список маршрутов приложения wiki
urlpatterns = [
    path('register/', register, name = 'register'),
    path('', user_login, name = 'login'),
    path('signup/', signup, name = 'signup'),
    path('logout/', user_logout, name = 'logout'),
    # path('', index, name = 'home'),
    #при обращении к пустой строке будет вызван index
    path('home/', HomeWiki.as_view(), name = 'home'),
    # path('category/<int:category_id>/', get_category, name = 'category'),
    path('category/<int:category_id>/', CategoryWiki.as_view(), name = 'category'),
    path('wiki/<int:pk>/', ViewWiki.as_view(), name = 'view_wiki'),
    # path('wiki/add-wiki/', CreateWiki.as_view(), name = 'add_wiki'),
    path('wiki/add-wiki/', add_wiki, name = 'add_wiki'),
]



