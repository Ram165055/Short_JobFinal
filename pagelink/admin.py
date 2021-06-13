from django.contrib import admin
from .models import Destination
from .models import Article
from .models import Post

# Register your models here.
admin.site.register(Destination)
admin.site.register(Article)
admin.site.register(Post)

