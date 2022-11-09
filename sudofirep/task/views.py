from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response
from .models import Customer, User
from .serializer import UserSerializer,CustomerSerializer
# from django.core.mail import send_mail
# import threading


# class HandleNotifications(threading.Thread):

#     def __init__(self, message, subject, recipient_list):
#         self.message = message
#         self.subject = subject
#         self.recipient_list = recipient_list
#         threading.Thread.__init__(self)

#     def run(self):
#         from_email = 'codes.environment@gmail.com'
#         send_mail(self.subject, self.message,from_email,self.recipient_list, fail_silently=False)
class CustomerViewset(viewsets.ModelViewSet):
    serializer_class= CustomerSerializer
    def get_queryset(self):
        customer = Customer.objects.all()
        return customer
    def create(self, request, *args, **kwargs):
        customer_data = request.data

        new_user = User.objects.create(
            first_name=customer_data["user"]["first_name"], last_name=customer_data["user"]["last_name"], email=customer_data["user"]["email"], mobile_no=customer_data["user"]["mobile_no"])
        new_user.save()

        new_customer = Customer.objects.create(
            profile_number=customer_data["profile_number"], user=new_user)
        new_customer.save()
        serializer = CustomerSerializer(new_customer)

        return Response(serializer.data)
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    def get_queryset(self):
        
        user = User.objects.all()
        return user

# class PostsViewSet(viewsets.ModelViewSet):
#     serializer_class = PostsSerializer

    # def send_email(self, message, subject, recipient_list):
    #     from_email = 'codes.environment@gmail.com'
    #     send_mail(subject, message,from_email,recipient_list, fail_silently=False)


    # def get_queryset(self):
    #     posts = Posts.objects.all()
    #     return posts


    # def create(self, request, *args, **kwargs):
    #     post_data = request.data

    #     new_rate = PostsRates.objects.create(
    #         likes=post_data["rates"]["likes"], dislikes=post_data["rates"]["dislikes"])
    #     new_rate.save()

    #     new_post = Posts.objects.create(
    #         post_title=post_data["post_title"], post_body=post_data["post_body"], rates=new_rate)
    #     new_post.save()
    #     # self.send_email("this a notification", "Notification",['codes.environment@gmail.com',])
    #     # HandleNotifications("this a notification", "Notification",['codes.environment@gmail.com',]).start()
    #     serializer = PostsSerializer(new_post)

    #     return Response(serializer)


# class PostsRatesViewSet(viewsets.ModelViewSet):
#     serializer_class = PostsRatesSerializer

#     def get_queryset(self):
#         rates = PostsRates.objects.all()
#         return rates

# Create your views here.
