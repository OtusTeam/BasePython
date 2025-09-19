from django.contrib import admin
from .models import Post, Comment, Author, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "author", "rating", "tag_list")
    ordering = ["rating", "title"]
    list_filter = ("author", "tags")
    search_fields = ["title", "content"]
    search_help_text = "Введите слово для поиска в заголовке или контенте"

    # fields = ('title', 'content', 'author', 'rating', 'tags')
    fieldsets = (
        ("Основная информация", {"fields": ("title", "content")}),
        (
            "Дополнительная информация",
            {
                "fields": ("author", "rating", "tags"),
                "classes": ("collapse",),
            },
        ),
    )

    @admin.action(description="Увеличить рейтинг на 1")
    def increase_rating(self, request, queryset):
        for post in queryset:
            post.rating += 1
            post.save()
        self.message_user(request, f"{queryset.count()} постов обновлено")

    actions = [increase_rating]

    # readonly_fields = ('rating',)

    def tag_list(self, obj):
        return ", ".join(tag.name for tag in obj.tags.all())


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name",)
    ordering = ["-name"]


admin.site.register(Author, AuthorAdmin)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    ordering = ("name",)
    search_fields = ("name",)
    search_help_text = "Введите слово для поиска в тэге"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("text", "author", "post")
    ordering = ("post", "author")
    search_fields = ("text",)
    search_help_text = "Введите слово для поиска в тексте"
