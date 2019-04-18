from django.shortcuts import (render,
                              get_object_or_404)
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models  import Post
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin


def Blog_home(request):
    context={
        'posts':Post.objects.all(),
        'title':'Index',
    }
    return render(request,'blog/Blog_home.html',context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/blog_home.html'# <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'# <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5
    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

# def Blog_Details(request,blog_id):
#     context={
#         'post':Post.objects.get(id=blog_id),
#     }
#     return render(request,'blog/blog_detail.html',context)
#
class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']

    def get_success_url(self):
        return reverse('Blog_home')

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False

    def get_success_url(self):
        return reverse('Blog_home')

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/blog'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    # def get_success_url(self):
    #     return reverse('Blog_home')

# def Blog_home(request):
#     return HttpResponse("<h1>This is Django Blog Website")
# def Blog_about(request):
#      return HttpResponse("<h1>This is Blog Website about")

def Blog_about(request):
     return render(request,'blog/Blog_about.html')
