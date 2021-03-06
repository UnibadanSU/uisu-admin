from django.contrib import admin

from news.models import Executive, Article, Profile, Representative, Tag

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    model = Tag


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    model = Article

    list_display = (
        "id",
        "title",
        "subtitle",
        "slug",
        "publish_date",
        "published",
    )

    list_filter = (
        "published",
        "publish_date",
    )


    list_editable = (
        "title",
        "subtitle",
        "slug",
        "publish_date",
        "published",
    )


    search_fields = (
        "title",
        "subtitle",
        "slug",
        "body",
    )


    prepopulated_fields = {
        "slug": (
            "title",
            "subtitle",
        )
    }


    date_hierarchy = "publish_date"
    save_on_top = True

@admin.register(Executive) 
class ExcecutivesAdmin(admin.ModelAdmin):
    model = Executive

class RepresentativeAdmin(admin.ModelAdmin):
    model = Representative