from django.views.generic import DetailView, TemplateView
from .models import FlatPage


class FlatPageView(DetailView):
    template_name = 'flat-page.html'
    model = FlatPage
    slug_field = 'url'
    slug_url_kwarg = 'url'
    context_object_name = 'flat_page'


class FlatPageIndex(TemplateView):
    template_name = 'flat-page.html'

    def get_context_data(self, **kwargs):
        context = super(FlatPageIndex, self).get_context_data(**kwargs)
        index_list = FlatPage.objects.filter(url='index')
        if len(index_list) > 0:
            context['flat_page'] = index_list[0]
        return context
