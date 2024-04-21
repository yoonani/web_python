from django.contrib import admin
# admin interface에 등록
from blog.models import Post, Profile, Tag

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile

@admin.register(Tag)
class Tagadmin(admin.ModelAdmin):
    model = Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post

    # To make browsing and editing posts more fluid, you customize a post’s details with these special variables:

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