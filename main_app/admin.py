from django.contrib import admin
from .models import Yorkie, Feeding, Toy

# Register your models here.
admin.site.register(Yorkie)
admin.site.register(Feeding)
admin.site.register(Toy)