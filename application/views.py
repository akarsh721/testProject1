from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import RegisterUser,userQuestion
from application.forms import RegisterUserForm,userQuestionForm
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth import authenticate

#for Mail
from django.core.mail import send_mail
from myproject1 import settings

#for sms
import json
import requests
import random



# Create your views here.
def index(request):
    loggedinUserName = request.session.get('loggedInUser')
    if request.method == 'POST':
        if request.POST.get('Signup') == 'Signup':
            userform = RegisterUserForm(request.POST,request.FILES)

            if userform.is_valid():
                userform.save()
                print("Successfully Registered!")
                messages.add_message(request,messages.SUCCESS,"Successfully Registered! Please Login to continue")

                #SEND MAIL
                # useremail = request.POST['username']
                # mail_subj = 'Registration Successful, Welcome User'
                # mail_msg = f"Hello {useremail}, \n Thank You for registering with us. \n This is system generated mail , do not reply to this. "
                # mail_from = settings.EMAIL_HOST_USER
                # mail_to = [useremail,]
                # send_mail(mail_subj,mail_msg,mail_from,mail_to)


                #SEND SMS
                # mention url
                #Enter Number field and pass num here to activate this
            
                '''url = "https://www.fast2sms.com/dev/bulk"
                usercontact = request.POST['contact']
                otp = random.randint(1111,9999)
                # create a dictionary
                my_data = {
                    # Your default Sender ID
                    'sender_id': 'FSTSMS',
                    
                    # Put your message here!
                    'message': f'This is a Confirmation message. \n Thank you for registration \n You default PIN is : {otp}',
                    
                    'language': 'english',
                    'route': 'p',
                    
                    # You can send sms to multiple numbers
                    # separated by comma.
                    'numbers': usercontact	
                }

                # create a dictionary
                headers = {
                    'authorization': '1cX8LUYqWiTv2xJONr4ZKyAH0dsn6MamfEGDejhQ7p5BkzFlgC0VDoNQJAleiK7am2OPF6bMEjYyUwvd',
                    'Content-Type': "application/x-www-form-urlencoded",
                    'Cache-Control': "no-cache"
                }

                # make a post request
                response = requests.request("POST",
                                            url,
                                            data = my_data,
                                            headers = headers)
                #load json data from source
                returned_msg = json.loads(response.text)

                # print the send message
                print(returned_msg['message'])'''
                
                                    
            else:
                print(userform.errors)

    #     elif request.POST.get('Login') == 'Login':
    #         # print("In Login")
    #         username = request.POST['username']
    #         password = request.POST['password']

    #         loginCheck = RegisterUser.objects.filter(username = username , password = password)
    #         if loginCheck:
    #             print("Loggedin successfully!!")
    #             request.session['loggedInUser'] = username
    #             return redirect("home")
    #         else:
    #             print("Invalid Credentials!")
    # else:
    #     userform = RegisterUserForm()
    return render(request,'index.html',{'user':loggedinUserName})


def home(request):
    loggedInUser = request.session.get('loggedInUser')
    if loggedInUser:
        userinfo = RegisterUser.objects.get(username = loggedInUser)
        name = userinfo.firstName
        userid = userinfo.id
        # Ucountry = userinfo.country
        # print(name)

        if request.method == 'POST':
            newUserQuestionForm = userQuestionForm(request.POST,request.FILES)

            if newUserQuestionForm.is_valid():
                newUserQuestionForm.save()
                print("Query uploaded successfully")
                messages.add_message(request,messages.SUCCESS,"Query submitted successfully!")
                return redirect("/home")

            else:
                print(userQuestionForm.errors)
                messages.add_message(request,messages.ERROR,userQuestionForm.errors)

        else:
            newUserQuestionForm = userQuestionForm()
        return render(request,'home.html',{'user_name':loggedInUser,'name':name,'userid':userid})
        
    else:
        return render(request,'home.html')


def userlogout(request):
    logout(request)
    return redirect("/")


def fetchqueries(request):
    loggedInUsername = request.session.get('loggedInUser')
    if loggedInUsername:
        userinfo = RegisterUser.objects.get(username = loggedInUsername)
        queryobject = userQuestion.objects.filter(queriedBy = loggedInUsername)
    # print(queryobject)
        return render(request,'fetchqueries.html',{'queryobject':queryobject,'username':loggedInUsername,'userinfo':userinfo})
    else:
        return render(request,'fetchqueries.html',{'username':loggedInUsername})


def deleteQuery(request,id):
    delquery = userQuestion.objects.get(pk = id)
    delquery.delete()
    return redirect("/fetchqueries")

def updateProfile(request,id):
    userinfo = RegisterUser.objects.get(pk=id)
    username = userinfo.firstNames
    print(username)

    if request.method == 'POST':
        updateform = RegisterUserForm(request.POST,instance=userinfo)

        if updateform.is_valid():
            updateform.save()
            print("Form updated successfully!")
            
            return HttpResponseRedirect("/home")

        else:
            print(updateform.errors)
            messages.add_message(request,messages.ERROR,updateform.errors)

    else:
        updateform = RegisterUserForm(instance=userinfo)
    return render(request,'updateProfile.html',{'userinfo':userinfo,'user_name':username})


def about(request):
    loggedInUser = request.session.get('loggedInUser')
    return render(request,'about.html',{'username':loggedInUser})


def contact(request):
    loggedInUser = request.session.get('loggedInUser')
    if loggedInUser:
        userinfo = RegisterUser.objects.get(username = loggedInUser)
        return render(request,'contact.html',{'username':loggedInUser,'userinfo':userinfo})
    else:
        return render (request,'contact.html',{'username':loggedInUser})


def writeUs(request):
    return render(request,'contact_writeUs.html')

def userlogin(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pswd = request.POST['password']

        loginCheck = RegisterUser.objects.filter(username = uname , password = pswd)

        if loginCheck:
            request.session['loggedInUser'] = uname
            messages.add_message(request,messages.SUCCESS,'Logged in successfully')
            print("Login Successful")
            return redirect("/home")
        else:
            messages.add_message(request,messages.ERROR,'Invalid Credentials')
            print("Invalid Credentials")
    return render(request,'login.html')


def registerUser(request):
    if request.method == 'POST':
        registerform = RegisterUserForm(request.POST)

        if registerform.is_valid():
            registerform.save()
            # for user
            messages.add_message(request,messages.SUCCESS,'Successfully Registered! Please Login to continue')
            # for console
            print("Register Successful")
            # Email and sms
        else:
            ers = registerform.errors
            messages.add_message(request,messages.ERROR,ers)
            print(ers)
    else:
        registerform = RegisterUserForm()
    return render(request,'signup.html')
