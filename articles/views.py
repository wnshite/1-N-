from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Article

# Create your views here.
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()

    context = {
        'form': form,
    }

    return render(request, 'create.html', context)

def index(request):
    articles = Article.objects.all()

    context = {
        'articles' : articles,
    }

    return render(request, 'index.html', context)

def detail(request, id):
    article = Article.objects.get(id=id)

    context = {
        'article' : article,
    }

    return render(request, 'detail.html', context)

def update(request, id):
    article = Article.objects.get(id=id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid(): # 새로운 정보만 is_valid로 검사.
            form.save()
            return redirect('articles:detail', id=id)

    else:
        form = ArticleForm(instance=article)

    context = {
        'form':  form,
    }
    return render(request, 'update.html', context)

def delete(request, id):
    # 데이터를 찾아서 지우고 index로 보내기
    article = Article.objects.get(id=id)
    article.delete()
    
    return redirect('articles:index')
