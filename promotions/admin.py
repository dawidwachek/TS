from django.contrib import admin
from .models import Coupon, Reflink


@admin.register(Reflink)
class ReflinkAdmin(admin.ModelAdmin):
    list_display = ['reflink_id', 'name_user', 'uses_reflink']
    readonly_fields = ["reflink_id","created_at", 'uses_reflink']
    list_filter = ['name_user']
    search_fields = ['name_user', 'reflink_id']

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['coupon_id', 'coupon_name','is_active','uses_coupon', 'type_coupon','max_value_coupon','value_coupon', 'max_uses_coupon', 'zero_amount']
    readonly_fields = ["coupon_id","created_at",'uses_coupon']
    list_filter = ['type_coupon','zero_amount','is_active']
    search_fields = ['coupon_id', 'coupon_name']