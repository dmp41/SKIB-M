from django.contrib import admin
from .models import *

admin.site.register(Product)
admin.site.register(Type_pay)
admin.site.register(Provider)
admin.site.site_header = "Панель администрирования"
admin.site.index_title = "Заказы"