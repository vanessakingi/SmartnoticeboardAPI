from board.models import users, images, text
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from passlib.hash import django_pbkdf2_sha256 as password_handler
import pytz
import datetime
from board import help


@api_view(['POST'])
def create_user(request):
    """
    Create user
    -----
        {
            user_id:1,
            full_name:veek
            username:vk
            email:vk@gmail.com
            department: TIE
            password: mypassword
        }
    """
    try:
        user = users(
            full_name=request.data['full_name'],  
            username=request.data['username'], 
            email=request.data['email'],
            department=request.data['department'],
            password=make_password(request.data['password']),
        )
        user.save()
        success = {
	        'message':'success',
	        'status_code':200
	    }
        return Response(success)    
    except BaseException as e:

        error={
            'status_code':500,
            'message':'error:'+ str(e),
            'data':{
           }
        }
        return Response(error)


@api_view(['POST'])
def create_image(request):
    """
    Create image
    -----
        {
            image_name:vk
            start_date:3/3/2018
            stop_date: 8/3/2018
            urgent: 1
        }
    """
    try:
        img = help.base64decoding(
        	pictures=request.data['image_name'], file_type='png'
        )
        image = images( 
            image_name=img['newName'], 
            start_date=request.data['start_date'],
            stop_date=request.data['stop_date'],
            urgent=request.data['urgent'],
            
        )
        image.save()
        success={
	        'message':'success',
	        'status_code':200
	    }
        return Response(success)
            
    except BaseException as e:

        error={
            'status_code':500,
            'message':'error:'+ str(e),
            'data':{
           }
        }
        return Response(error)



@api_view(['POST'])
def create_text(request):
    """
    Create text
    -----
        {
            text_id:1.0,
            text:hello world
            start_date:3/3/2018
            stop_date: 8/3/2018
        }
    """
    try:
        
        text = text(
            text_id=request.data['text_id'],
            text=request.data['text'],   
            start_date=request.data['start_date'],
            stop_date=request.data['stop_date'],
            
        )
        text.save()
        success={
	        'message':'success',
	        'status_code':200
	    }
        return Response(success)
            
    except BaseException as e:

        error={
            'status_code':500,
            'message':'error:'+ str(e),
            'data':{
           }
        }
        return Response(error)

@api_view(['GET'])
def display_notices(request):
    try:
        img = images.objects.all()
        data=[]
        for imgs in img:
        	details={
        		'image_name':imgs.image_name,
        		'start_date':imgs.start_date,
        		'stop_date':imgs.stop_date,
        		'urgent':imgs.urgent,
        	}
        	data.append(details)
        success={
	    	'data':data,
	        'message':'success',
	        'status_code':200
	    }
        return Response(success)
            
    except BaseException as e:

        error={
            'status_code':500,
            'message':'error:'+ str(e),
            'data':{
           }
        }
        return Response(error)


@api_view(['POST'])
def login_user(request):
    """
    Create text
    -----
        {
            username:jsdcac
            password:jcmadcbnasc
        }
    """
    try:
        user_id=request.data['username']
        user_input_pass=request.data['password']
        user=users.objects.get(username=user_id)

        if password_handler.verify(user_input_pass, user.password):
            success={
                'data':{
                    'user_id':user.user_id,
                    'full_name': user.full_name,
                    'username': user.username,
                    'email':user.email,
                    'depart':user.department
                },
                'status_code':200,
            }
                
            return Response(success)

        else:
            success={
                'message':'Error',
                'status_code':500
            }
                
            return Response(success)    
    except BaseException as e :
        
        error={
            'status_code':500,
            'message':'error'+str(e),
        }
        return Response(error)


