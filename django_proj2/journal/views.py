
from django.shortcuts import render
from django.http import HttpRequest
from journal.models import Post, Comment



def index(request: HttpRequest):
    qs = Post.objects.all()
    return render(request, "journal/journal_list.html", {
        "journal_list": qs,
    })


def post_detail(request: HttpRequest, pk):
    post = Post.objects.get(pk=pk)
    return render(request, "journal/journal_detail.html", {
        "post": post,
    })

def comment_detail(request: HttpRequest, pk):
    comment = Comment.objects.get(pk=pk)
    return render(request, "journal/journal_detail.html", {
        "comment": comment,
    })