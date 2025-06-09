from django.urls import path
from .views import TaskListCreateView, TaskDetailView, RegisterView,UserListView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:id>/', TaskDetailView.as_view(), name='task-detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
