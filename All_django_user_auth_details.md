#### <U>**USER AUTH GUIDE USING DJANGO**</u>

- ***

#### **<u>Below model classes Present in django.contrib.auth.models module </u>**

1- ***<u>User</u>*** - inherit ***AbstractUser***

2- ***<u>AbstractUser</u>*** -- inherit ***AbstractBaseUser and PermissionMixin***

3- ***<u>Permission</u>***

4- ***<u>Permission Mixin</u>***

5- ***<u>Group</u>***

6- ***<u>UserManager</u>*** --->inherit ***BaseUserManager***

	- This UserManager class provide 2 function which can help in creating user
    create_user(username="",email=None,password=None,**extra_data)
    create_superuser(username="",email=None,password=None,**extra_data)
 	with_perms(perms,is_active=True,active_superclass=True,backend=None,obj=None)

7- ***<u>AnonymousUser</u>*** - means a user having below property 
	
    - id=None
    - pk=None
    - is_active=None
    - is_staff=None
    - is_superuser=None
    - username= ""
    - groups=EmptyManager(Group)
    - user_permission=EmptyManager(Group)
    
- ***

<u>FORMS AVAILABLE in DJANGO_AUTHENTICATION</u>:-

- ***<u>UserCreationForm(forms.ModelForm)</u>*** used for registration of a new user having no super user or staff access only have active user Access

- ***<u>UserChangeForm(forms.ModelForm)</u>*** used for changing the user info in the profile page 

- ***<u>AuthenticationForm(forms.Form)</u>***:-normal form Api used for Authenticating the user after user logged in 

- ***<u>PasswordResetForm</u>(forms.Form)***:-used whenwe want to set the password if uiser forgot its password this form used to render the field to enter the email so that it can send an email onbehalf

- ***<u>SetPassword(forms.Form)</u>***:-use to render the Page when the user get the email and click on  the link and it will get the form to update the password field without entering the old password 

- ***<u>PasswordChangeForm(SetPasswordForm)</u>***:-this inherit the setpassword form and this will be used when the user logged in and want to change the password and here user need to provide the old password in order to change the password and password been changed then user will be logged out and need to relogin again 

- ***<u>AdminPasswordChangeForm(SetPasswordForm)</u>***:-used for changing the password for the user in the Admin webpage but user must be superuser or staff member 

- ***

##### ** URL FOR USING THE AUTH BACKEND **

```
# url available in django.contrib.auth.urls.py
#view available in django./contrib.auth.viws.py
# here the name is back reference name  
urlepatterns=[
	
    path("login/",views.LoginView.as_view(),name="login"),
    path("logout/",views.LogOutView.as_view(),name="logout"),
    path("password_change",views.PasswordChangeView.as_view(),name="password_chage"),
    path("password_change/done/",views.PasswordChangeDoneView.as_view(),name="password chage_done"),
    path("password_rest",views.PasswordResetView.as_view(),name="password reset"),
    path("password_reset/done/",views.PasswordResetDoneView.as_view(),name="password_reset_done"),
   path("reset/<uidb64>/<token>/",views.PasswordResetConfirmView.as_view(),name="password_reset_confirm")
    path("reset/done",views.PasswordResetCompleteView.as_view(),name="password_reset_complete")
    
    ]

```


- ***


##### METHOD OD USER OBJECT #####

```
1- <user obj>.get_username()-->provide the username we can also get using <user obj>.username(not recomended)

2- <user obj>.get_full_name()-->provide the full name of user

3- <usr obj>.get_short_name()--->provide the first name

4- <userobj>.set_password(raw_password)-->take raw pass and hash it and save it 

5- <usr obj>.check_password(raw_password)--> take the raw pass and check thats been valid or not by comparing with the hashed password 

6- <user obj>.set_unusable_password()-->set to unusable hash which can't be decode 

7- <user obj>.has_usable_password()
   -->reurtn True if the password set using set_password 
   --> return False if the password set using the set_unusable_password

8- <user>.get_user_paermission(obj=None/User obj)
	--> return set of user_permission of  all the user if obj=None
 	--> return that specific user_permission if the particular user obj provided 
    
9- <user>.get_group_paermission(obj=None/User obj)
	--> return set of group permission for all the user if obj=None
 	--> return that specific group_permission if the particular user obj provided 
    
10- <user obj>.get_all_permission(obj=None/User obj)
	--> return set of group and user permission for all the user if obj=None
 	--> return that specific group and user permission if the particular user obj provided
    
11- <user obj>.has_perm(perm,obj=None/User obj)
	-->return True if user obj provided has the permission as perms
    -->for inactive user its always False
    ---> For superuser its always True
    ---> perms==<appname>.<permission code>
    
12- <user obj>.has_perms(perm_list,obj=None/User obj)
	-->return True if user obj provided has all the permission as perms_list
    -->for inactive user its always False
    ---> For superuser its always True
    ---> perms==<appname>.<permission code>

-13 <user>.create_user(username="username",email=None,passoward=None,**extrafield)

	-create_user is method which belong to the UserManger class which is custom model manager of user Model 
    -this will create, save as well as return the user obj
    - also it will create user with is_active=True only
    -email will be lowercase while saving 

-14
-<user>.create_superuser(username="username",email=None,passoward=None,**extrafield)

	-create_superuser is method which belong to the UserManger class                which is custom model manager of user Model 
    -this will create, save as well as return the user obj
    - also it will create user with is_active=True and is_staff=True         and is_superuser=True
    -email will be lowercase while saving 

-15
- <userobj>.with_perms(perms,is_active=True,include_superuser=True,backend=None,obj=None)

	this too belong to the UserManager model manager of User model class method 
    but here in this case user object will be return if the user has the perms mentioned
    perms cbe in the form of <app>.<permcode>
 
```

##### FIELD OF USER MODEL #######


```
username->max 150 char (required)
password->(required)
first_name-->150(optional)
last_name-->250(optional)
email--->(blank=True)(optional)
date_joined-->optional(date time field)
last_login-->optional(date time field)
groups-->M-2-M field relating the Group model
user_permission-M-2-M firld related to user_permission group
is_authenticated-->optional(if authenticated the True else False)
is_anonymous-->optional(if not authenticated then True else False)
is_active=True/False
is_staff=True/False
is_superiser=True/False

```



##### FIELD OF GROUP MODEL #######

```
name-->155 char(required)
permission-->M2M field with Permission model  

```

##### FIELD OF Permision MODEL #######

```
name-->255 char(required)
content_type==>a reference django_content_type db table which contain all model info (required)
codename==100 char of permission code name which wil be user for validating perms (required)


```

