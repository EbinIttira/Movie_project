from django.urls import path
from. import views
app_name='movieapp'
urlpatterns = [
    path('',views.display,name='display'),
    path('movie/<int:movie_id>/',views.detail,name='detail'),
    path('add/',views.add,name='add'),
    path('delete/<int:pk>/',views.MovieDeleteview.as_view(),name='delete'),
    path('update/<int:id>/',views.update,name='update'),
]
