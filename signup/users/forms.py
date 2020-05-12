# from django import forms
# from django.contrib.auth import (
#     authenticate,
#     get_user_model
#
# )
# User = get_user_model()
#
#
# class UserRegisterForm(forms.Form):
#     class Meta:
#         fields = [
#             'first_name',
#             'last_name',
#             'username',
#             'email',
#             'password'
#         ]
#
#     def clean(self, *args, **kwargs):
#         username = self.cleaned_data.get('username')
#         email = self.cleaned_data.get('email')
#         # if password != email2:
#         #     raise forms.ValidationError("Emails must match")
#         email_qs = User.objects.filter(email=email)
#         user_qs = User.objects.filter(username=username)
#         if email_qs.exists():
#             raise forms.ValidationError(
#                 "This email has already been registered")
#         if user_qs.exists():
#             raise forms.ValidationError(
#                 "This username has already been registered")
#         return super(UserRegisterForm, self).clean(*args, **kwargs)