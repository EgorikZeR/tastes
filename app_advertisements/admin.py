from django.contrib import admin
from .models import Advertisement

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','price','created_date','update_at','auction','image']
    list_filter = ['auction','created_at']
    actions = ['action_auction_as_false','action_auction_as_true']
    fieldsets = (
        ('общее', {
            'fields': ('title','description','image')
        }),
        ('финансы', {
            'fields': ('price', 'auction'),
            'classes':['collapse']
        })
    )

    @admin.action(description='убрать возможность торга')
    def action_auction_as_false(self,request,queryset):
        queryset.update(auction=False)

    @admin.action(description='дать возможность торга')
    def action_auction_as_true(self, request, queryset):
        queryset.update(auction=True)


admin.site.register(Advertisement,AdvertisementAdmin)
