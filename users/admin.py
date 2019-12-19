# django
from django.contrib import admin

# local
from users.models import Profile
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # Esto es para que en la lista del admin nos muestre en ese orden y esos datos
    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    
    # Con esto hacemos que esos atributos sean clickeables
    list_display_links = ('pk', 'user')

    # Los valores en esta lista dejará que sean editables desde la visualización general
    list_editable = ('phone_number', 'website')

    # Campos que funcionarán para búsqueda, para el caso de user no podemos directo del objeto
    # sino de un atributo
    search_fields = (
        'user__email', 
        'user__first_name',
        'user__last_name',
        'phone_number'
    )

    list_filter = (
        'created',
        'modify',
        'user__is_active',
        'user__is_staff'
    )