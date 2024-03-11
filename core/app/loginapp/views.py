
from app.user_management.models import CustomUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from rest_framework.authtoken.models import Token
from .models import Student
from .serializers import LoginSerializer
from .serializers import studentserializer
from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import TokenAuthentication
from rest_framework import  permissions
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, OAuth2Authentication




class LoginAPI(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    def post(self, request):
        data = request.data
        serializer = LoginSerializer(data=data)
        if not serializer.is_valid():
            return Response({'status': False, 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
        user = CustomUser.objects.get(email=serializer.data['email'])
        if not user.check_password(serializer.data['password']):
            return Response({'status': False, 'message': 'Incorrect password'}, status=status.HTTP_400_BAD_REQUEST)
        
        # token =Token.objects.get_or_create(user=user)
        # print(token)'token': str(token)
        return Response({'status': True, 'message': 'User logged in' }, status=status.HTTP_201_CREATED)
    

class StudentAPI(APIView):
        authentication_classes = [OAuth2Authentication]
        permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
        def post(self,request):
            data = request.data
            serializer = studentserializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)  
            return Response(serializer.errors) 
        def get(self,request):
            try:
                print(request.user)
                obj =Student.objects.all()
                serializer=studentserializer(obj,many=True)
                return Response(serializer.data)
            except Exception as e:
                return Response({'status':False,
                                "message":"error"})
            
