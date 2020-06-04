from django.contrib import admin
from django.contrib.auth.models import User
from .models import TblAdp,TblCategory,SubCategories
from django.contrib.auth import get_user_model
# Register your models here.

from .models import notify,TblAdp
class disp(admin.ModelAdmin):
    list_display=('notif','day','hrs','min')
class adpdisp(admin.ModelAdmin):
    list_display=('adp_id','firstname','email')
class fd(admin.ModelAdmin):
    list_display=('sub_category','category')

admin.site.register(notify,disp)
admin.site.register(TblAdp,adpdisp)
admin.site.register(TblCategory)
admin.site.register(SubCategories,fd)
