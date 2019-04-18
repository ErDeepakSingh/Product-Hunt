from django.contrib import admin

# Register your models here.
from . import models as product_models

admin.site.register(product_models.Product)