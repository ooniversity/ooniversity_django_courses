# ~*~ coding: utf-8 ~*~
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse_lazy, reverse
from datetime import datetime
from django.template import RequestContext, loader
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from pybursa_emails.models import Mail
from pybursa import settings
from django.core.mail import send_mail

class MailForm(ModelForm):
    class Meta:
        model = Mail
        fields = 'sender_name', 'message_theme', 'message', 'sender_email'


class MailList(ListView):
    model = Mail


class MailCreate(CreateView):
    model = Mail
    form_class = MailForm
    initial = {'message_date': datetime.now()}
#    template_name = 'mail_add.html'

    def get_context_data(self, **kwargs):
        context = super(MailCreate, self).get_context_data(**kwargs)
        context['shead'] = 'Введите параметры сообщения'
        context['prompt'] = 'Сохранить данные'
        return context
    def get_success_url(self):
        return reverse('pybursa_emails:mail_add_redirect', kwargs={'mail_id': self.object.pk})

def mail_add_redirect(request, mail_id=None):

    mail_list = Mail.objects.all()

    theme = ''

    if mail_id:
        s = mail_list.get(pk=mail_id)
        theme= s.message_theme

    text = u"Сообщение с темой (" + theme + u') '+ u" сохранено в базе данных"
    template = loader.get_template('pybursa_emails/mail_list.html')
    context = RequestContext(request, {
        'mail_list': mail_list,
        'text': text,
    })

    return HttpResponse(template.render(context))


class MailDelete(DeleteView):
    model = Mail
    template_name = 'pybursa_emails/mail_delete.html'

    def get_context_data(self, **kwargs):
        context = super(MailDelete, self).get_context_data(**kwargs)
        self.course = Mail.objects.get(pk=self.kwargs['pk'])

        context['shead'] = 'Вы действительно хотите удалить сообщение '
        context['prompt'] = 'Удалить'

        return context
    def get_success_url(self):
        return reverse('pybursa_emails:feedback')

def mail_send(request,mail_id):

    rsadm = settings.ADMINS

    mail_list = Mail.objects.all()
    mail_s = mail_list.get(pk = mail_id)
    s_email = mail_s.sender_email
    theme = mail_s.message_theme

    for rs in rsadm:
        body = u'Доброго времени суток, '+ rs[0]+ u'!\n'
        body += mail_s.message
        send_mail(theme, body, s_email, [rs[1]], fail_silently=False)

    mail_s.send_date = datetime.now()
    mail_s.save()
    text = u"Сообщение с темой (" + theme + u') '+ u" отправлено"
    template = loader.get_template('pybursa_emails/mail_list.html')
    context = RequestContext(request, {
        'mail_list': mail_list,
        'text': text,
    })

    return HttpResponse(template.render(context))





