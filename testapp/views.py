from django.shortcuts import render
from testapp.models import details
from testapp.serialize import detailserialize
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import requests
from rest_framework import generics

# Create your views here.
@api_view(['POST'])
def savedata(request):
	if request.method=="POST":
		saveserialize=detailserialize(data=request.data)
		if saveserialize.is_valid():
			saveserialize.save()
			return Response(saveserialize.data,status=status.HTTP_201_CREATED)
			return Response(saveserialize.data,status=status.HTTP_400_BAD_REQUEST)



def insertdata(request):
	if request.method=="POST":
		name=request.POST.get('name')
		position=request.POST.get('position')
		mobile=request.POST.get('mobile')
		address=request.POST.get('address')
		data={'name':name,'position':position,'mobile':mobile,'address':address}
		headers={'content-Type':'application/json'}
		read=requests.post('http://127.0.0.1:8000/savedata',json=data,headers=headers)
		return render(request,'login2.html')
	else:
		return render(request,'login2.html')