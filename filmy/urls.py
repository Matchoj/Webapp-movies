
from django.contrib import admin
from django.urls import path
from movies.views import allmovies, newmovie,editmovie, deletemovie, logout_view, allcommnets,deletecoment
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('allmovies/',allmovies,name="all"),
    path('new_movie/',newmovie,name="new"),
    path('edit/<int:id>',editmovie,name='edit'),
    path('delete/<int:id>',deletemovie,name="delete"),
    path('deletecom/<int:id>',deletecoment,name="deletecom"),
    path("login/", auth_views.LoginView.as_view(),name="login"),
    path("logout/", logout_view,name="logout"),
    path("comments/<int:id>", allcommnets, name ="comments")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
