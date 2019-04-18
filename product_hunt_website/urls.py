
from django.conf.urls import (url,
                              include)
from django.contrib import admin
from products import views as products_views
from . import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', products_views.products_home,name='home'),
    url(r'^account/', include('account.urls')),
    url(r'^products/', include('products.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^users/', include('users.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
