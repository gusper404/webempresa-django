from django.contrib import admin
from .models import Link

# Register your models here.
class LinkAdmin(admin.ModelAdmin):
	readonly_fields = ('created', 'updated')
	list_display = ('name', 'key', 'url')

	def get_readonly_fields(self, request, obj=None):
		if request.user.groups.filter(name="Personal").exists():
			return ('key', 'name')
		else:
			return ('created', 'updated')

	def get_list_display(self, request, obj=None):
		if request.user.groups.filter(name="Personal").exists():
			return ('name', 'url')
		else:
			return ('name', 'key', 'url')
				

admin.site.register(Link, LinkAdmin)
