from django.contrib import admin
from .models import ServiceRequest

class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('email', 'customer_name', 'status', 'created_at', 'updated_at')
    list_filter = ('status',)
    search_fields = ('email', 'customer_name')  # Enables search
    list_per_page = 25  # Paginate results for better performance
    ordering = ('-created_at',)  # Orders by latest request first
    readonly_fields = ('created_at', 'updated_at')  # Prevents manual edits
    date_hierarchy = 'created_at'  # Enables date-based filtering

admin.site.register(ServiceRequest, ServiceRequestAdmin)
