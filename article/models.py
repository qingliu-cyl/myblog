from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from slugify import slugify
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class ArticleColumn(models.Model):
    column = models.CharField(max_length = 200)
    created = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.column

class ArticlePost(models.Model):
    title = models.CharField(max_length = 200)
    slug = models.SlugField(max_length = 500)
    column = models.ForeignKey(ArticleColumn,related_name = "article_column")
    body = RichTextUploadingField()
    created = models.DateTimeField(default = timezone.now())
    updated = models.DateTimeField(auto_now = True)
    
    class Meta:
        ordering = ["title"]
        index_together = (('id','slug'),)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:article_detail",args = [self.id,self.slug])

