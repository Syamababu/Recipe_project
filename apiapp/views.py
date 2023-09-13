from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from apiapp.models import Company, Employee
from apiapp.serializers import comapnyserializer,employeeserializer
from rest_framework import viewsets
from rest_framework.decorators import api_view,permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated

#authentications

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CustomAuthTokenlogin(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

# FUNCTION BASED VIEWS ------- USING DECORATOR
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def company_list(request):
     if request.method=='GET':
          comp=Company.objects.all()
          serializer=comapnyserializer(comp,many=True)
          return JsonResponse(serializer.data,safe=False)
     
     elif request.method=='POST':
          tutorial_data = JSONParser().parse(request)
          serializer=comapnyserializer(data=tutorial_data)
          if serializer.is_valid():
               serializer.save()
               return JsonResponse(serializer.data)
          return JsonResponse(serializer.errors)

@api_view(['GET','POST','PUT','DELETE'])
@permission_classes([IsAuthenticated])
def company_details(request,pk):
     if request.method=='GET':
          compa=Company.objects.get(pk=pk)
          serializer=comapnyserializer(compa)
          return JsonResponse(serializer.data)
     
     elif request.method=='PUT':
          compa=Company.objects.get(pk=pk)
          ins_data=JSONParser().parse(request)
          serializer=comapnyserializer(compa,data=ins_data)
          if serializer.is_valid():
               serializer.save()
               return JsonResponse(serializer.data)
          else:
               return JsonResponse(serializer.errors)
          
     elif request.method=='DELETE':
          compa=Company.objects.get(pk=pk)
          compa.delete()
          return JsonResponse({'msg':'data deleted'}) 
               

     

          
     

# api using APIView================== CLASS BASED VIEWS
class comapnyviewset(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        comp=Company.objects.all()
        serializer=comapnyserializer(comp,many=True)
        return Response({'comapny list':serializer.data})

    def post(self, request, format=None):
            serializer = comapnyserializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
    
class comapnyviewsetdetails(APIView):
     permission_classes = [IsAuthenticated]
     def get(self,request,pk):
          compa=Company.objects.get(id=pk)
          serializer=comapnyserializer(compa)
          return Response(serializer.data)
     
     def delete(self,request,pk):
          comp=Company.objects.get(id=pk)
          comp.delete()
          return Response({'msg':'comapny deleted'})

     def put(self,request,pk):
          comp=Company.objects.get(id=pk)
          serializer=comapnyserializer(comp,data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
          return Response(serializer.errors)
     

# api using ModelViewSet==================
class EmployeeViewSet(viewsets.ModelViewSet):
     queryset=Employee.objects.all()
     serializer_class=employeeserializer
     permission_classes=[IsAuthenticated]


     
