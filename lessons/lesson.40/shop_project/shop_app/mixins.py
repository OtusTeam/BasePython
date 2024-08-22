class PageTitleMixin:
    page_title = 'Shop'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.page_title
        # print(context)
        return context
