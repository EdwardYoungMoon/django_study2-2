from django.contrib import admin
from django.urls import path, include

# from bookmark.views import BookmarkDV, BookmarkLV

from mysite.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('bookmark/', include('bookmark.urls')),
    path('blog', include('blog.urls')),

    path('', HomeView.as_view(), name='home')

    # # class-based views
    # path('bookmark/', BookmarkLV.as_view(), name='index'),
    # path('bookmark/<int:pk>/', BookmarkDV.as_view(), name='detail'),
]
