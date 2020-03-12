from django.test import TestCase
from django.core import mail
from books import forms

class TesTform(TestCase):
    def valid_contact_form_sends_email(self):
        form=forms.ContactForm({'name':"Ssali Jonathan",'message':"Hi there"})
        self.assertTrue(form.is_valid())
        with self.assertLogs('main.forms',level='INFO') as cm:
            form.send_mail()
        self.assertEqual(mail.outbox()[0].subject,'Site Message')

        self.assertGreaterEqual(len(cm.output),1)


    def test_invalid_coontact_us_form(self):
        form=forms.ContactForm({'message':"Hi THere"})
        self.assertFalse(form.is_valid())
