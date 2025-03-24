from django.contrib import admin

from django_celery_results.models import TaskResult
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from .models import Post, Comment, Tag, Author, AuthorProfile


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'rating', "created_at")
    ordering = ('-rating', '-created_at' )
    list_filter = ('author', 'rating')
    search_fields = ('title', 'content')
    search_help_text = "Search by title or content"

    # fields =  ('title', 'content')
    # readonly_fields = ('rating',)

    fieldsets = (
        ('Main options', {
            'fields': ('title', 'content', 'author')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('rating', )
        })
    )

    @admin.action(description="Set rating to 10")
    def set_rating_10(self, request, queryset):
        # queryset.update(rating=10)
        for post in queryset:
            post.rating = 10
            post.save()
        self.message_user(request, "Rating set to 10")

    actions = [set_rating_10]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']
    search_fields = ['name']
    search_help_text = "Search by name"




@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['text', 'author', 'post']
    ordering = ['author', 'post']
    search_fields = ['text', 'post']
    search_help_text = "Search by text or post"

    fields =  ('text', 'post', 'author')
    readonly_fields = ('created_at',)

    @admin.action(description="Delete comments")
    def delete_comments(self, request, queryset):
        count = queryset.count()
        queryset.delete()
        self.message_user(request, f"{count} comments deleted")

    actions = [delete_comments]


@admin.register(AuthorProfile)
class AuthorProfiletAdmin(admin.ModelAdmin):
    list_display = ['author', 'bio', "website"]
    ordering = ['author']
    search_fields = ['bio', "website"]
    search_help_text = "Search by bio or website"


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']
    search_fields = ['name']
    search_help_text = "Search by name"

    def profile_bio(self, obj):
        return obj.profile.bio if obj.profile else "No bio"
    profile_bio.short_description = "Bio"


admin.site.register(Author, AuthorAdmin)
