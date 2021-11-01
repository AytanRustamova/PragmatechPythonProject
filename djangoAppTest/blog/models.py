from django.db import models

# Create your models here.
class Blog(models.Model):

    CATS ={
        (1, 'sport'),
        (2, 'fashion'),
        (3, 'technology'),
        (4, 'politics')
    }

    title = models.CharField(max_length=127, null=True, blank=True)
    text = models.TextField(help_text='Bura esas melumati daxil edin...')
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=63, verbose_name='Muellif', )
    cats = models.IntegerField(max_length=100, choices=CATS, default=1)
    blog_tags = models.ManyToManyField('Tag')



    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
        ordering = ('created_at',)
    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=63, null=True, blank=True)

    def __str__(self):
        return self.title


        
 