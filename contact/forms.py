from django import forms

class ContactForm(forms.Form):
    name = forms.CharField()
    senders_name = forms.CharField(max_length=255)
    subject = forms.CharField(max_length=255)
    body = forms.CharField(widget=forms.Textarea)
    senders_email = forms.EmailField()
    date_created =  forms.DateTimeField()


    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass
