from django.contrib import admin
from .models import Post, Movie, Collection, Comment


# Register your models here.

class SlugAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post)
admin.site.register(Movie, SlugAdmin)
admin.site.register(Collection, SlugAdmin)
admin.site.register(Comment)
