from django.contrib import admin

# Register your models here.
from .models import Cities, CarCategories, Car, Rental, PaymentMethod, Payment


@admin.register(Cities)
class Cities(admin.ModelAdmin):
    list_display = ("id", "city")


class CarAdminInline(admin.TabularInline):
    model = Car
    extra = 0


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("id", 'category', 'brand', 'model', 'description', 'license_plate', 'available')
    list_display_links = ('brand',)
    list_filter = ('category', 'available',)


@admin.register(CarCategories)
class CarCategories(admin.ModelAdmin):
    list_display = ("id", "nameCategory", "available")
    inlines = [CarAdminInline]


@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ("id", 'car', 'renter', 'start_date', 'end_date', 'price')


@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ("id", 'method',)


@admin.register(Payment)
class Payment(admin.ModelAdmin):
    list_display = ("id", 'rental', 'amount', 'payment_date', 'payment_method',)
