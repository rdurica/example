from django.contrib import admin

"""
Example of module registration

@admin.register(ApplicationType)
class ApplicationTypeAdmin(admin.ModelAdmin):
    list_display = ('some_field',)
    list_display_links = ('some_field',)
    search_fields = ('some_field',)
    list_per_page = 50
"""
