from django.db import models
from django.utils import timezone
from auth_users.models import CustomUser as User

def user_directory_path(instance, filename):
    return 'blog/{0}/{1}'.format(instance.id, filename)

class Post(models.Model):
    class PostsObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')
    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    thumbnail = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='created', null=False, unique=True)
    created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts_user')
    published = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=options, default='draft')
    objects = models.Manager()
    postsobjects = PostsObjects()
    
    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title