from django.shortcuts import render
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.views.generic.edit import CreateView
from mail.models import Mail
from django.core.urlresolvers import reverse_lazy


class MailCreateView(CreateView):
	template_name = 'mail/feedback.html'
	model = Mail
	success_url = reverse_lazy('mail:feedback')

	def form_valid(self, form):
		super_valid = super(MailCreateView, self).form_valid(form)
		to_list = [address for (login, address) in settings.ADMINS]
		send_mail(
			subject=self.object.subject, 
			message=self.object.message, 
			from_email=self.object.email, 
			recipient_list=to_list,
		) 
		msg = "Email to {} was sent!".format(to_list)
		messages.success(self.request, msg)
		return super_valid
		