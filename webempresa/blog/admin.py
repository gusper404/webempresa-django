from django.contrib import admin
from .models import Post, Category

# Register your models here.

class PostAdmin(admin.ModelAdmin):
	readonly_fields = ['created', 'updated']
	list_display = ('title', 'author', 'published', 'post_categories')
	ordering = ('author', 'published')
	search_fields = ('title','author__username', 'categories__name')
	date_hierarchy = 'published'
	list_filter = ('author__username','categories__name')

	def post_categories(self, obj):
		return ", ".join([c.name for c in obj.categories.all().order_by("name")])
	post_categories.short_description = "Categorías"

admin.site.site_header = "Administrador"
admin.site.register(Post, PostAdmin)
admin.site.register(Category)