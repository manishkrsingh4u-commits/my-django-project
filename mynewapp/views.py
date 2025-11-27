from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

# If you set DEFAULT_AUTHENTICATION_CLASSES globally, you only need permission_classes below.
# But here I demonstrate explicit per-view authentication/permission usage.

# 1) Public view (open to everyone)
@api_view(['GET'])
@permission_classes([AllowAny])
def public_view(request):
    return Response({"message": "This is public — no JWT something we have changed for testing purpos"})

# 2) Class-based view protected with JWT
from rest_framework_simplejwt.authentication import JWTAuthentication

class ProtectedView(APIView):
    # explicitly require JWT authentication only for this view
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # request.user will be available
        return Response({
            "message": "Protected endpoint — you are authenticated",
            "user": str(request.user.username)
        })

# 3) Function-based view protected with JWT
@api_view(['GET'])
@authentication_classes([JWTAuthentication])  # enforces JWT auth on this view
@permission_classes([IsAuthenticated])
def protected_func_view(request):
    return Response({"message": "Protected function view", "user": request.user.username})
