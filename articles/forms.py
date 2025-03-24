from django.forms import ModelForm
from .models import Article, Comment

class ArticleForm(ModelForm):
    class Meta():
        model = Article
        fields = '__all__'
        
class CommentForm(ModelForm):
    class Meta():
        model = Comment
        # fields = '__all__'

        # fields -> 추가할 피드 목록
        # fields = ('content', )

        # exclude -> 제외할 피드 목록
        exclude = ('article', )
