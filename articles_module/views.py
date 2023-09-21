from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import ListView
from .models import article, articles_category


# Create your views here.

class article_list_View(ListView):
    template_name = 'articles_module/article_list_View.html'
    model = article
    paginate_by = 5
    context_object_name = 'article_list_View'

    def get_queryset(self, **kwargs):
        query = super(article_list_View, self).get_queryset()
        category_main = self.kwargs.get('category')  # category url
        if category_main is not None:
            query = query.filter(Article_and_Category_Relation__url_title__iexact=category_main)
        return query


def article_category_component(request: HttpRequest):
    article_category = articles_category.objects.filter(is_active=True, parent=None)
    return render(request, 'articles_module/component/component.html', context={
        'article_category': article_category
    })
