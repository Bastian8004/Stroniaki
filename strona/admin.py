
from django.contrib import admin
from strona.models import Main, About_us, Blog, Post


admin.site.register(Main)
admin.site.register(About_us)

class PostInline(admin.TabularInline):
    model = Post

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    inlines = [
        PostInline,
    ]

