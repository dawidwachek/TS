from django.contrib import admin
from .models import Coupon, Reflink


@admin.register(Reflink)
class ReflinkAdmin(admin.ModelAdmin):
    list_display = ['reflink_id', 'name_user']
    readonly_fields = ("reflink_id","created_at")

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['coupon_id', 'coupon_name']
    readonly_fields = ("coupon_id","created_at")