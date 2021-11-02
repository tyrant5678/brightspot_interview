from django.db import models

# Create your models here.
class Comment(models.Model):
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    comment_text = models.CharField(max_length=255)
    comment_author = models.CharField(max_length=255)
    date_pub = models.DateTimeField('date published')
    """
    Returns the queryset of comments for which the given comment is parent
    """
    def get_children(self):
        return Comment.objects.filter(parent_comment=self)
    """
    Returns a boolean value indicating whether or not a given comment has children
    """
    def has_children(self):
        return len(Comment.objects.filter(parent_comment=self)) > 0
    
    def get_id(self):
        return self.id


class Article(models.Model):
    article_title = models.CharField(max_length=255)
    article_text = models.TextField()
    article_author = models.CharField(max_length=255)
    date_pub = models.DateTimeField('data published')
