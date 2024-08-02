from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Department,Doctor,contactus
from .forms import BookingForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from django.urls import reverse

# Create your views here.
def home1(request):
    return HttpResponse("Hello World")
def home(request):
     return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def department(request):
    dept_dict={
         'depts': Department.objects.all()    
               }
    return render(request,'department.html',dept_dict)
def doctor(request):
    doc_dict={
        'docs': Doctor.objects.all()    
              }
    return render(request,'doctors.html',doc_dict)

from django.shortcuts import render,get_object_or_404

def doctor_list(request,dept_slug=None):
    depts=Department.objects.all()
    docs=Doctor.objects.all()

    if dept_slug:
         dep_name=get_object_or_404(Department,slug=dept_slug)
         docs=docs.filter(dep_name=dep_name)
    else:
         dep_name=None
    context={
         'dep_name':dep_name,
         'depts':depts,
         'docs': docs
        }
    return render(request,'doctors.html',context)

def booking(request):
    if request.method=="POST":
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
    form=BookingForm()
    dict_form={
        'form':form
    }
    return render(request,'booking.html',dict_form)

def contact(request):
    if request.method=='GET':
        return render(request,'contact.html')
    elif request.method=='POST':
        name1=request.POST['name']
        email1=request.POST.get('email',None)
        message1=request.POST.get('message',None)
       
        cont=contactus(name=name1,email=email1,message=message1)
        cont.save()
        # return HttpResponse('<h1>Message saved successfully</h1>')
        return render(request,'success.html')


class Tasklistview(ListView):
    model=Department
    template_name='department.html'
    context_object_name='dept'

class TaskDetailview(DetailView):
    model=Department
    template_name='clsdetail.html'
    context_object_name='dept'

class TaskUpdateView(UpdateView):
    model=Department
    template_name='update.html'
    fields=('dep_name','dep_description')
    # success_url=reverse_lazy('home')

    def get_success_url(self):
        return reverse_lazy('cbdetail',kwargs={'pk':self.object.id})

class TaskDeleteView(DeleteView):
    model= Department
    template_name='delete.html'
    success_url=reverse_lazy('pg5')

class TaskCreateView(CreateView):
    model=Department
    template_name='create.html'
    fields='__all__'
    success_url=reverse_lazy('pg1')

def login(request):
    if request.method == 'GET':
        if 'logged_in' in request.COOKIES and 'username' in request.COOKIES:
            context= {
                'username':request.COOKIES['username'],
                'login_status':request.COOKIES.get('logged_in'),
            }
            return render(request,'home.html',context)
        else:
            return render(request,'login.html')
    if request.method == "POST":
        username=request.POST.get('email')
        context = {
            'username':username,
            'login_status':'TRUE'
        }
        response = render(request,'home.html',context)

        response.set_cookie('username', username)
        response.set_cookie('logged_in', True)
        return response

def home(request):
    if 'logged_in' in request.COOKIES and 'username' in request.COOKIES:
        context = {
            'username':request.COOKIES['username'],
            'login_status':request.COOKIES.get('logged_in'),
        }
        return render(request,'home.html',context)
    else:
        return render(request,'login.html')
    
def logout(request):
    response=HttpResponseRedirect(reverse('login'))
    response.delete_cookie('username')
    response.delete_cookie('logged_in')
    return response
