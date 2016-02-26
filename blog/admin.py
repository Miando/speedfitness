from django.contrib import admin
from .models import Post
from django.contrib.flatpages.admin import FlatpageForm, FlatPageAdmin
from .models import FlatPage
from .models import FlatPageOld


admin.site.unregister(FlatPageOld)
admin.site.register(FlatPage)
admin.site.register(Post)
