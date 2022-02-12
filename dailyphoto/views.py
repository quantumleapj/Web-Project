

# from time import timezone
from wsgiref.util import request_uri
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404,redirect
from dailyphoto.models import Profile
from django.contrib.auth import get_user_model
from .forms import PostForm, CustomUserChangeForm, ProfileForm, CommentForm
from .models import Post
from django.utils import timezone
from django.http import JsonResponse

# from PIL import Image

# 주소 index 
def index(request):
    """
    dailyphoto 게시물 출력
    """
    post_list = Post.objects.order_by('-create_date')

    context = {'post_list': post_list}
    return render(request, 'dailyphoto/post_list.html', context)

# post 상세
def detail(request, post_id):
    
    post  = get_object_or_404(Post, pk=post_id) # 예외일때 404에러 발생
    # get_object_or_404 <- 오류 화면 구성
    context = { 'post': post}
    return render(request, 'dailyphoto/post_detail.html', context)

# 글 업로드 함수
# @login_required(login_url='common:login')
def post_create(request): 
  """
  upload
  """
  now_url=request.get_host()
  print('현재 페이지 주소?')
  print(now_url)
  print(request.get_full_path)
  print(request.path)

  if request.method== "POST":
    print('request method is post')
    form = PostForm(request.POST)
    if form.is_valid():
      post = form.save(commit=False)
      # photo_file=request.FILES['photo']
      # print(photo_file)
      if 'photo' in request.FILES:
        post.photo=request.FILES['photo']
      else:
        pass
        # post.photo="/Logo/DailyphotoLog.png"
        # post.photo="DailyphotoLog.png"
      # post.photo=request.FILES['id_photo']
      post.author= request.user
      post.create_date=timezone.now()
      post.save()
      print('post save made')
      print(form.as_p)
      return redirect('dailyphoto:index')
    else:
      print('form is not valid')
  else:

    print('request method is not post its get')
    form=PostForm()
  print(form.as_p)

  context = {'form': form ,
  'now_url':request.path
  }
  return render(request, 'dailyphoto/upload_page.html', context )


# 댓글 기능
@login_required(login_url='common:login')
def comment_create(request, post_id): 
    post = get_object_or_404(Post, post_id) 
    if request.method == "POST":
      form = CommentForm(request.POST) 
      if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.create_date = timezone.now()
        comment.post = post
        comment.save()
        return redirect('pybo:detail', post_id=post.id)
    else:
      form = CommentForm() 
      context = {'form': form}
    return render(request, 'pybo/comment_form.html', context)








#프로필화
def profile(request, username):
    person = get_object_or_404(get_user_model(), username = username )
    post_list = Post.objects.order_by('-create_date')
    post_photo = Post.objects.filter(author_id = request.user.id)
    
    
    context = {
      'post_list': post_list ,
       'person': person,
       'post_photo' : post_photo
       }

    return render(request, 'dailyphoto/profile.html', context)



def modify_profile(request):
    if request.method == 'POST':
      user_change_form = CustomUserChangeForm(request.POST, instance=request.user)
      profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
      if user_change_form.is_valid() and profile_form.is_valid():
          user = user_change_form.save()
          profile_form.save()
          return redirect('dailyphoto:profile', user.username)
      return redirect('dailyphoto:profile')
    else:
        user_change_form = CustomUserChangeForm(instance=request.user)
        profile, create = Profile.objects.get_or_create(user=request.user)
        profile_form = ProfileForm(instance=profile)
        return render(request, 'dailyphoto/profile_form.html', {
            'user_change_form': user_change_form,
            'profile_form': profile_form
        })

def detail(request):
  pass

  

  



