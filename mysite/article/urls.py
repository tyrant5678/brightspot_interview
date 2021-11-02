from django.urls import path

from . import views

app_name = 'article'
urlpatterns = [
    path('',views.articleView.as_view(), name='article'),
    path('submitComment', views.submitComment, name='submitComment'),
    path('submitReply/<int:comment_id>', views.submitReply, name='submitReply'),
]