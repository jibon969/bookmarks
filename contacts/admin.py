from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ['email', 'phone']

    class Meta:
        model = Contact
        fields = '__all__'


admin.site.register(Contact, ContactAdmin)
