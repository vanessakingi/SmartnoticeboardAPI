from django.urls import include, path
from board import notice


urlpatterns = [
    
    #User routes
    path('createuser/', notice.create_user),
    path('createimages/', notice.create_image),
    path('createtext/', notice.create_text),
    path('display_notices/', notice.display_notices),
    path('login', notice.login_user)
]