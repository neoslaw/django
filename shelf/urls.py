from django.conf.urls import include, url

from .views import ( AuthorListView,AuthorDetailView, BookListView, BookDetailView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^autorzy/$', AuthorListView.as_view(), name='author-list'),
    url(r'^autorzy/(?P<pk>\d+)/$', AuthorDetailView.as_view(), name='author-detail'),

    url(r'^ksiazki/$', BookListView.as_view(), name='book-list'),
    url(r'^ksiazki/(?P<pk>\d+)/$', BookDetailView.as_view(), name='book-detail'),

]