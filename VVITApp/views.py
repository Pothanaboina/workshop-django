from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def demo(request):
	return HttpResponse("WELCOME TO APSSDC WORKSHOP")

def greet(sd,n):
	return HttpResponse(f"Hi WELCOME {n}")
def stdnt(request,a,b,c="VVIT"):
	return HttpResponse(f"college name:{c}<br/> student name:{a} <br> student age:{b}")
def ky(s):
	return HttpResponse("<h3> WELCOME User</h3>")
def my(sd,n): 
	return HttpResponse(f"<h1>hi <span	style ='color:red'>{n}</span></h1>")
def emp(t,es,en):
	return HttpResponse("<style>#w{color:blue}</style><h2>welcome <span style='color:red'>"+en+"</span></h2><h3>salary:<span id='w'>"+str(es)+"</span></h3>")

										
def ry(self):
	return HttpResponse	("<script>alert('Hi,User WELCOME');</script>")
def hello(self,m):
	return HttpResponse	(f"<script>alert('Hi {m}');</script>")

def student(request, sname, srollno, sage, sbranch):
    return HttpResponse(f"<script>alert('hi {sname}');</script>"
                        f"<table border=1>"
                        f"<tr><th>Student Roll No</th><th>Student Age</th><th>Student Branch</th></tr>"
                        f"<tr><td>{srollno}</td><td>{sage}</td><td>{sbranch}</td></tr>"
                        f"</table>")
def my_fun(request):
 	return render(request,'sample.html')
def ml(request,a):
 	return render(request,'sam.html',{'z':a})
def fun(request,ename,esal):
	return render(request,'employ.html',{'l':ename,'m':esal})
def good(self,e):
	return HttpResponse(f"welcome to the {e}")
def stdform(request):
	if request.method=="POST":
		a=request.POST['rn']
		b=request.POST['sn']
		c=request.POST['sy']
		d=request.POST['sb']
		return render(request,'stdata.html',{'x':a,'y':b,'l':c,'m':d})
		
	return render(request,'student.html')

