# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from students.models import Student
from django import forms
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail, send_mass_mail
from django.views.generic.edit import FormView, CreateView
from mails.models import Mail
from django.core.urlresolvers import reverse_lazy


class MailCreateView(CreateView):
    template_name = 'mails/mail.html'
    model = Mail
    success_url = reverse_lazy('mails:send-mail')

    def form_valid(self, form):
        self.application = form.save()
        address_list = [address for (login, address) in settings.ADMINS]
        send_mail(
            subject=self.application.subject,
            message=self.application.mail_text,
            from_email=self.application.address_sender,
            recipient_list=address_list,
        )
        messages.success(self.request, u'Письмо отправлено по адресу {}'.format(address_list))

        return super(MailCreateView, self).form_valid(form)





#Создание формы по модели
#class MailForm(forms.ModelForm):
#    class Meta:
#        model = Mail


#Класс для создания студента
#class MailFormView(CreateView):
#    model = MailForm
#    success_url = reverse_lazy('students:student-list')

#    def form_valid(self, form):
#        self.application = form.save()
#        send_mail(
#            subject=self.application.subject,
#            message=self.application.mail_text,
#            from_email=self.application.address_sender,
#            recipient_list=[address for (login, address) in settings.LIST_OF_EMAIL_RECIPIENTS],
#        )
#        messages.success(self.request, u'Письмо отправлено')
#        return super(ContactFormView, self).form_valid(form)


#Класс для создания студента
#class MailFormView(FormView):
#    model = MailForm
#    success_url = reverse_lazy('students:student-list')

#    def form_valid(self, form):
#        self.application = form.save()
#        messages.success(self.request, u'Студент {} {} успешно добавлен'.format(self.application.surname, self.application.name))
#        return super(MailFormView, self).form_valid(form)

    #Добавляем название страницы шаблона HTML в контекстные данные
    #def get_context_data(self, **kwargs):
    #    context = super(StudentCreateView, self).get_context_data(**kwargs)
    #    context['page_title'] = u"Создание студента"
    #    return context
