from django.contrib import admin
from .models import Comment, AddNews


class ContantAdmin(admin.ModelAdmin):
    list_display =('id', 'title','username','created_on')
    list_display_links=('id', 'title','username','created_on')
    # list_editable = ('to_show')
    list_per_page = 25

class AddNewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'title', 'created_on')
    list_display_links=('id', 'name','title','created_on')
    list_per_page = 25


admin.site.register(Comment, ContantAdmin)
admin.site.register(AddNews, AddNewsAdmin)