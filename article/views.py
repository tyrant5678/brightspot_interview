from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.urls import reverse
from article.models import Comment, Article
import datetime
class articleView(TemplateView):
    template_name = 'article.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments_list'] = Comment.objects.filter(parent_comment=None).order_by('-date_pub')
        context['article'] = Article.objects.first()
        print(context)
        return context
def submitComment(request):
    try:
        if request.POST['comment_text'] != '':
            c = Comment(comment_text=request.POST['comment_text'], date_pub=datetime.datetime.now(), comment_author='Anonymous')
        c.save()
    except Exception as e:
        print('error')
        print(e)
        return render(request, 'article.html', {
            'comments_list':Comment.objects.order_by('-date_pub'),
            'article': Article.objects.all()[0]
        })
    return HttpResponseRedirect(reverse('article:article'))

def submitReply(request, comment_id):
    try:
        if request.POST['reply_text'] != '':
            c = Comment(comment_text=request.POST['reply_text'], date_pub=datetime.datetime.now(), comment_author='Anonymous', parent_comment=Comment.objects.get(pk=comment_id))
        c.save() 
    except Exception as e:
        print('reply error')
        print("reply exception:",e)
        return render(request, 'article.html', {
            'comments_list':Comment.objects.filter(parent_comment=None).order_by('-date_pub'),
            'article': Article.objects.all()[0]
        })
    return HttpResponseRedirect(reverse('article:article'))