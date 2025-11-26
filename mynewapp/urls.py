from django.urls import path
from mynewapp.views import public_view,ProtectedView,protected_func_view

urlpatterns = [
    path('public/',public_view, name='public'),
    path('protected/',ProtectedView.as_view(), name='protected'),
    path('protected-func/',protected_func_view, name='protected_func'),
]