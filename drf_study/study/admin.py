from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from drf_study.study.models import Study, CustomUser


@admin.register(CustomUser)
class UserAdmin(DefaultUserAdmin):
    pass


@admin.register(Study)
class StudyAdmin(admin.ModelAdmin):
    fields = (
        'title',
        'category',
        'description',
        'created_date',
        'updated_date'
    )
    list_display = (
        'title',
        'category',
        'description',
        'created_date',
        'updated_date'
    )
    readonly_fields = (
        "created_date",
        "updated_date",
    )
