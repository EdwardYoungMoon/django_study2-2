from django.shortcuts import render
from bookmark.models import Bookmark
from django.views.generic import ListView, DetailView

class BookmarkLV(ListView):
    model = Bookmark
    template_name = 'bookmark_list.html'

class BookmarkDV(DetailView):
    model = Bookmark
    template_name = 'bookmark_detail.html'