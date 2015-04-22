# -*- coding: utf-8 -*-

from django.contrib import messages
from django.views.generic.edit import CreateView
from feedback.models import FeedbackMessage
from feedback.forms import FeedbackMessageForm


class FeedbackMessageCreateView(CreateView):
    model = FeedbackMessage
    template_name = 'feedback/feedback.html'
    form_class = FeedbackMessageForm
    success_url = '#'

    def get_context_data(self, **kwargs):
        context = super(FeedbackMessageCreateView, self)\
                       .get_context_data(**kwargs)
        context['page_title'] = u"Обратная связь"
        return context
    
    def form_valid(self, form):
        form = super(FeedbackMessageCreateView, self).form_valid(form)
        when = self.object.when
        messages.success(self.request, 
                 u'Сообщение с темой "{0}" отправлено администраторам сайта в {1}:{2}:{3}'\
                  .format(self.object.theme, when.hour+3, when.minute, when.second))
        return form



