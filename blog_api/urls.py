from django.urls import path
from .views import PostDetails, PostList

urlpatterns = [
    # path('<int:pk>/', PostDetails.as_view()),
    path('', PostList.as_view()),
]
