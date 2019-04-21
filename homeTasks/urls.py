from django.conf.urls import url,include
from django.views.generic import ListView, DetailView
from homeTasks.models import Article1

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Article1.objects.all().order_by("-date")[:20],template_name="homeTasks/posts.html")),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Article1, template_name = "homeTasks/post.html"))
]
