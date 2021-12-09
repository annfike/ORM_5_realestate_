from django.contrib import admin

from .models import Flat, Complaint, Owner


class OwnerInline(admin.TabularInline):
    model = Owner.flat.through
    raw_id_fields = ('owner', 'flat',)


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('owner', 'town','address')
    readonly_fields = ['created_at']
    list_display = (
        'address',
        'price',
        'new_building',
        'construction_year',
        'town',
    )
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    raw_id_fields = ('liked_by',)
    inlines = [OwnerInline,]


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('user', 'flat', 'text',)
    list_editable = ('flat', 'text',)
    raw_id_fields = ('flat',)
    

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('owner', 'owners_phonenumber', 'owner_pure_phone',)
    list_editable = ('owners_phonenumber', 'owner_pure_phone',)
    raw_id_fields = ('flat',)
    inlines = [OwnerInline,]
    exclude = ('flat',)