from django.db import models
from datetime import datetime
from django.contrib.auth.models import BaseUserManager,PermissionsMixin, AbstractBaseUser
from django.template.defaultfilters import slugify
from tinymce.models import HTMLField


class Categories(models.TextChoices):
    CLOUD = 'Cloud'
    SPACE = 'Space Sciences'
    AI = 'Artificial Intelligence'
    Opinion = 'Opinion'
    Tech = "Technology"
    
    
class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=255)
    category = models.CharField(max_length=50, choices = Categories.choices, default = Categories.SPACE)
    thumbnail = models.URLField(max_length = 200,null=False, blank=False, default="https://github.com/denniesbor/denniesbor.github.io/raw/assets/twist2/greg-jeanneau-9sxeKzuCVoE-unsplash.jpg")
    excerpt = models.CharField(max_length=120)
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

# Feedback info
class Feedback(models.Model):
    email= models.EmailField(max_length=150,unique=True)
    name = models.CharField(max_length=150)
    date_received = models.DateTimeField(default = datetime.now,blank=True)
    message = models.TextField(max_length=1000)
    
    def __str__(self):
        return self.name

class UserAccountManager(BaseUserManager):
    def create_user(self,email, name, password):
        if not email:
            raise ValueError('Users must have an email address')
        
        email = self.normalize_email(email)
        user = self.model(email = email, name = name) 
        user.set_password(password)
        user.save()
        
        return user
    
    def create_superuser(self, email, name, password):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not name:
            raise ValueError("User must have a full name")


        user = self.create_user(
            email= self.normalize_email(email),
            name= name,
            password= password,
        )
        user.is_admin= True
        user.is_staff= True
        user.is_superuser= True
        user.is_active = True
        user.save(using= self._db)
        return user
    
    
class UserAccount(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default= False)
    is_superuser = models.BooleanField(default= False)
    objects = UserAccountManager()

    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    
    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name
    
    def __str__(self):
        return self.email
    