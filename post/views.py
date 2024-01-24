from django.shortcuts import render


# Create your views here.

from .models import Post
from .forms import PostForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView



def post_list(request):
    all_posts= Post.objects.all()
    return render(request, 'post/post_list.html', {'all_posts':all_posts})



def post_detail(request , id):
    post = Post.objects.get(id=id)
    return render(request,'post/post_detail.html',{'post':post})



def post_create(request):
    if request.method == "POST":
       form = PostForm(request.POST)
       if form.is_valid():
           form.save()
       
    else:
        form = PostForm()  
    return render(request,'post/post_create.html',{'form':form})

def post_edit(request ,id):
    post = Post.objects.get(id=id)
    if request.method == "POST":
       form = PostForm(request.POST ,instance=post)
       if form.is_valid():
           form.save()
       
    else:
        form = PostForm(instance=post)  
    return render(request,'post/post_edit.html',{'form':form})







class PostList(ListView):
    model = Post  
    template_name = 'post/post_list.html'  
    
    
    
class PostDetail(DetailView):
    model = Post   
    
    
class PostUpdate(UpdateView) :
    model = Post
    fields =['title','content','email']
    template_name = 'post/post_edit.html'
    success_url = '/blog/cbv'   
    
    
    
class PostCreate(CreateView) :
    model = Post
    fields = ['title','content','created_at','published_at','email']
    template_name = 'post/post_create.html'
    success_url = '/blog/cbv'       
    
    