from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Lesson)
admin.site.register(Review)
admin.site.register(ForumCategory)
admin.site.register(ForumTopic)
admin.site.register(ForumPost)
