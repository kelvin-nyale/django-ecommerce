# from django.contrib.auth.backends import BaseBackend
# from django.contrib.auth import get_user_model
# from myApp import Users
#
# class EmailAuthenticationBackend(BaseBackend):
#     def authenticate(self, request, email=None, password=None):
#         users = get_user_model()
#         try:
#             user = Users.objects.get(email=email)
#             if user.check_password(password):
#                 return user
#         except Users.DoesNotExist:
#             return None
#
#     def get_user(self, user_id):
#         users = get_user_model()
#         try:
#             return Users.objects.get(pk=id)
#         except Users.DoesNotExist:
#             return None
