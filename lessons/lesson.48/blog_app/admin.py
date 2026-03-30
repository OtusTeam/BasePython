from django.contrib import admin
from .models import Post, Author, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "rating", "content", "author", "tag_list")
    ordering = ["-rating", "-author"]
    list_filter = ("rating", "author")
    search_fields = ("title", "content")
    search_help_text = "Введите часть заголовка или контента для поиска"

    def tag_list(self, obj):
        return ", ".join(tag.name for tag in obj.tags.all())

    tag_list.short_description = "Тэги"

    # fields = ('title', 'content', 'author', 'rating',  'tags')
    # readonly_fields = ('rating', )

    fieldsets = (
        ("Основаня информация", {"fields": ("title", "author")}),
        (
            "Дополнительная информация",
            {"fields": ("content", "rating", "tags"), "classes": ("collapse",)},
        ),
    )

    @admin.action(description="Увеличить рейтинг на 10")
    def edit_rating(self, request, queryset):
        for post in queryset:
            post.rating += 10
            post.save()

    actions = (edit_rating,)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "profil_bio")
    ordering = ("name",)

    search_fields = ("name",)
    search_help_text = "Введите часть имени для поиска"

    def profil_bio(self, obj):
        return obj.profile.bio if obj.profile else "Профиль отсутствует"

    profil_bio.short_description = "Профиль"


admin.site.register(Author, AuthorAdmin)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    ordering = ("name",)

    search_fields = ("name",)
    search_help_text = "Введите часть тэга для поиска"
