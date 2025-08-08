from django.db import models


class NewsSource(models.Model):
    name = models.CharField(max_length=255)
    rss_url = models.URLField(unique=True)
    country = models.CharField(max_length=100, default="Argentina")
    # RSS tag mappings
    title_tag = models.CharField(max_length=100, default="title")
    link_tag = models.CharField(max_length=100, default="link")
    published_tag = models.CharField(max_length=100, default="pubDate")
    summary_tag = models.CharField(max_length=100, default="description")

    def __str__(self):
        return self.name


# Represents a group of articles about the same event
class NewsEvent(models.Model):
    topic = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.topic


class NewsArticle(models.Model):
    source = models.ForeignKey(NewsSource, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    link = models.URLField()
    published = models.DateTimeField()
    summary = models.TextField(blank=True)
    news_event = models.ForeignKey(
        NewsEvent, null=True, blank=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.title
