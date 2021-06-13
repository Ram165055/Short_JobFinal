
from .models import Destination
from .utils import get_plot,get_histo_plot,get_pie_plot
from .models import Post

from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login
from django.contrib import messages
import csv
from django.http import HttpResponse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn import svm
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from django.views.generic import ListView, DetailView
from . models import Article
from .forms import CommentForm

# Create your views here.

def index(request):
    return render(request,'index.html')
def login(request):
    # print("here1 {0}".format(request))
    if request.method=='POST':
        # email=request.POST['email']
        password=request.POST['password']
        username=request.POST['name']
        # print("here3 {0} {1}".format(email,password))
        user=auth.authenticate(username=username,password=password)
        # print("here4 {0}".format(user))
        if user is not None:
            auth.login(request, user)
            # print("here5")
            return redirect('/')
        else:
            messages.info(request,'invalid credential')
            return redirect('login')
    else:
        return render(request,'login.html')

def register(request):
    if request.method=='POST':
        # first_name=request.POST['first_name']
        username=request.POST['name']
        password1=request.POST['password']
        # password2=request.POST['password2']
        email=request.POST['email']

        user=User.objects.create_user(username=username,password=password1,email=email)
        user.save()
        print('user created')
        return redirect('login')


    else:
        return render(request,'register.html')


def dash(request):
    dests=Destination.objects.all()
    return render(request,'dash.html',{'dests': dests})


def post(request):
    if request.method=='POST':
        name=request.POST['name']
        img=request.FILES['img']
        desc=request.POST['desc']
        skill=request.POST['skill']
        price=request.POST['price']
        location=request.POST['location']
        phone=request.POST['phone']
        
        
        user=Destination.objects.create(name=name,img=img,desc=desc,skill=skill,price=price,location=location,phone=phone)
        user.save()
        return redirect('joblist')
    else:
        return render(request,'post.html')


def searchresult(request):
    query=request.POST['name']
    alpost=Destination.objects.filter(name__icontains=query)


    return render(request,'searchresult.html',{'alpost':alpost,'query':query})

def search(request):
    # user=request.GET['username']
    # user=auth.authenticate(username=username,password=password,email=email)
    # if request.user.is_authenticated:

        # return render(request,'profile.html',{'user':user})
        return render(request,'search.html')
    # else:
        # return redirect('login')
def logout(request):
    auth.logout(request)
    messages.info(request,'you are logout')
    return redirect('/')

def about(request):
    return render(request,'about.html')


def blog(request):
    return render(request,'blog.html')

def joblist(request):
    dests=Destination.objects.all()
    return render(request,'joblist.html',{'dests': dests})

def profile(request):
    return render(request,'profile.html')

def my_func(request):
    return HttpResponse(request, "this is on click")
    # document.getElementById('remove-heli-' + dest).style.visibility = 'hidden'



def csv_database_write(request):

    # Get all data from UserDetail Databse Table
    users = User.objects.all()

    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="csv_database_write.csv"'

    writer = csv.writer(response)
    writer.writerow(['username', 'password', 'email'])

    for user in users:
        writer.writerow([user.username, user.password, user.email])

    return response





def predict(request):
    return render(request,'prediction.html')

def filter_data(fileobj):
    #first drop unwanted columns
    fileobj = fileobj.drop(columns=['Username','Timestamp','Email'])
    #second giving short hand notations to the long name columns
    fileobj = fileobj.rename(columns={'Number of Jobs Performed': 'NJP', 'Number of Skills Added': 'NAS'},)
    #Third put more categorical values in gender column
    #But lets just comment this as this won't affect much more of our project
    gender = LabelEncoder()
    location = LabelEncoder()
    fileobj['Gender'] = gender.fit_transform(fileobj['Gender'])
    fileobj['Location'] = location.fit_transform(fileobj['Location'])
        #this line of code gives integer value to genders and locations:
        # female  - 0               bhilai  - 0              raipur  -  3
        # male    - 1               durg  - 1
        # others  - 2               others    - 2
    #fourth dropping unwanted data or false data
    fileobj = fileobj.drop(fileobj.index[(fileobj['Age']) >= 90])
    return fileobj

def predict_NAS(ffile,a=[]):
    x = ffile.drop(['NAS'], axis=1)
    y = ffile['NAS']
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0)
    s = StandardScaler()
    x_train = s.fit_transform(x_train)
    x_test = s.fit_transform(x_test)
    clf = svm.SVC()
    clf.fit(x_train, y_train)
    pred = clf.predict(x_test)
    # classification_report(y_test,pred) return this also if asked or required
    # confusion_matrix(y_test,pred) return this also if asked or required
    # accuracy_score(y_test,pred) prints the accuracy of the model
    a = s.transform(a)
    b = clf.predict(a)
    # print(classification_report(y_test,pred))
    # print(ffile.plot(x='Age',y='NJP',kind='hist'))
    return b[0],(accuracy_score(y_test,pred)*100)


def gplot():
    users = User.objects.all()
    print(users)
    x=[x.username for x in users]
    y=[y.email for y in users]
    print(plt.plot(x, y, label = "line 1"))
    plt.show()


def predict_Loc(ffile,a=[]):
    x = ffile.drop(['Location'], axis=1)
    y = ffile['Location']
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0)
    s = StandardScaler()
    x_train = s.fit_transform(x_train)
    x_test = s.fit_transform(x_test)
    clf = svm.SVC()
    clf.fit(x_train, y_train)
    pred = clf.predict(x_test)
    # classification_report(y_test,pred) return this also if asked or required
    # confusion_matrix(y_test,pred) return this also if asked or required
    # accuracy_score(y_test,pred) prints the accuracy of the model
    a = s.transform(a)
    b = clf.predict(a)
    return b[0],accuracy_score(y_test,pred)



def predict_result(request):
    # val1=int(request.GET['num1'])
    # val2=int(request.GET['num2'])
    # res=val1+val2
    skill=int(request.POST['skill'])
    age=int(request.POST['age'])
    location=int(request.POST['location'])
    gender=int(request.POST['gender'])
    data=pd.read_csv('shortJobs_DB1.csv')
    data=filter_data(data)
    print(data)
    # res=gplot()
    res=predict_NAS(data,[[age,skill,gender,location]])
    # res=predict_Loc(data,[[age,skill,gender,location]])
    
    return render(request,'prediction.html',{'result1':res})




def show(request):
    data = pd.read_csv('shortJobs_DB1.csv')
    data = filter_data(data)
    data.drop_duplicates(keep= 'first', inplace=True)
    #plotting NJP vs Age graph
    x = [x for x in data['Age']]
    x.sort()
    y = [y for y in data['NJP']]
    chart0 = get_plot(x,y,'Graph 1','Age','NJP')

    #plotting Age vs NAS
    x = [x for x in data['Age']]
    x.sort()
    y = [y for y in data['NAS']]
    chart1 = get_plot(x, y, 'Graph 2', 'Age', 'NAS')

    #plotting NAS vs NJP
    x = [x for x in data['NAS']]
    x.sort()
    y = [y for y in data['NJP']]
    chart3 = get_plot(x,y, 'Graph 4', 'NAS', 'NJP')

    #plotting Location vs NAS
    x = [x for x in data['Location']]
    x.sort()
    y = [y for y in data['NAS']]
    chart4 = get_plot(x, y, 'Graph 5', 'Location', 'NAS')

    #plotting NJP vs Location
    x = [x for x in data['Location']]
    x.sort()
    y = [y for y in data['NJP']]
    chart5 = get_plot(x, y, 'Graph 6', 'NJP', 'Location')

    #histogram plotting NJP
    x= [x for x in data['NJP']]
    x.sort()
    chart6 = get_histo_plot(x,'Histogram 1','NJP')

    #histogram plotting NAS
    x=[x for x in data['NAS']]
    chart7 = get_histo_plot(x,'Histogram 2','NAS')

    #histogram pie Age
    data.drop_duplicates(subset=['Age'],keep= False, inplace=True)
    x=[x for x in data['Age']]
    x.sort()
    chart8 = get_pie_plot(x,'Piechart 1','Age')

    #description tab
    descr = data.describe()
    descr = descr.to_html()
    return render(request,'analysis.html',{'graph1':chart0,'graph2':chart1,
                                                        'graph4':chart3, 'graph5':chart4,'graph6':chart5,
                                                        'hgraph1':chart6, 'hgraph2':chart7, 'hgraph3':chart8, 'desc':descr})
    # return render(request,'analysis.html',{'graph1':chart0,'graph2':chart1,
    #                                                     'graph4':chart3, 'graph5':chart4,'graph6':chart5,
    #                                                     'hgraph1':chart6, 'hgraph2':chart7, 'hgraph3':chart8})







# class ArticleListView(ListView):
#     model = Article
#     template_name = 'home.html'


# class ArticleDetailView(DetailView):
#     model = Article
#     template_name = 'detail.html'




def frontpage(request):
	posts = Post.objects.all()

	return render(request, 'blog.html', {'posts': posts})

def post_detail(request,slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
    	form = CommentForm(request.POST)

    	if form.is_valid():
    		comment = form.save(commit=False)
    		comment.post = post
    		comment.save()

    		return redirect('post_detail', slug=post.slug)
    else:
    	form = CommentForm()

    return render(request, 'blog.html', {'post': post, 'form': form})