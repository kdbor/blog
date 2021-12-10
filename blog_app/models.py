from django.db import models
from datetime import datetime
from django.contrib.auth.models import BaseUserManager,PermissionsMixin, AbstractBaseUser
from django.template.defaultfilters import slugify


class Categories(models.TextChoices):
    CLOUD = 'cloud'
    SPACE = 'space'
    AI = 'ai'
    
    
class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    category = models.CharField(max_length=50, choices = Categories.choices, default = Categories.SPACE)
    thumbnail = models.ImageField(upload_to='photos/%Y/%m/%d')
    excerpt = models.CharField(max_length=150)
    month = models.CharField(max_length = 3)
    day = models.CharField(max_length = 2)
    content = models.TextField()
    featured = models.BooleanField(default=False)
    date_created = models.DateTimeField(default = datetime.now,blank=True)
    author = models.CharField(max_length=150,default = 'dkbor')
    
    def save(self, *args,**kwargs):
        original_slug = slugify(self.title)
        queryset = BlogPost.objects.all().filter(slug__iexact=original_slug).count()
        
        count = 1
        slug = original_slug
        
        while(queryset):
            slug = original_slug + '-' + str(count)
            count += 1
            queryset = BlogPost.objects.all().filter(slug__iexact=slug).count()
            
        self.slug = slug
        
        if self.featured:
            try:
                temp = BlogPost.objects.get(featured =True)
                if self != temp:
                    temp.featured = False
                    temp.save()
            except BlogPost.DoesNotExist:
                pass
        super(BlogPost, self).save(*args,**kwargs)
        
    def __str__(self):
        return self.title

# Feedback information
class Feedback(models.Model):
    email= models.EmailField(max_length=150,unique=True)
    name = models.CharField(max_length=150)
    date_received = models.DateTimeField(default = datetime.now,blank=True)
    message = models.TextField(max_length=1000)
    
    def __str__(self):
        return self.name

class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, password =None):
        if not email:
            raise ValueError('Users must have an email address')
        
        email = self.normalize_email(email)
        user = self.model(email = email, name = name) 

        user.set_password(password)
        user.save()
        
        return user
    
    
class UserAccount(AbstractBaseUser,PermissionsMixin):
    email= models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_staff= models.BooleanField(default=False)
    is_active= models.BooleanField(default=True)

    objects = UserAccountManager()

    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    
    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name
    
    def __str__(self):
        return self.email