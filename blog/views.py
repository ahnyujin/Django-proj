from django.shortcuts import render
from .forms import PostForm
from .test01 import test

def post_list(request):
    output = "HI"
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            output = test( request.POST.copy().get('text') )
    else:
        form = PostForm()
    return render(request, 'blog/post_list.html', {'form': form, 'output':output})
