from django.shortcuts import render

from articles.models import Article, Tags


def articles_list(request):
    template = 'articles/news.html'
    article = Article.objects.all().order_by('-published_at')
    scope = Tags.objects.all().order_by('-name')
    context = {'articles': article, 'scopes':scope}

    # # используйте этот параметр для упорядочивания результатов
    # # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    # ordering = '-published_at'

    return render(request, template, context)