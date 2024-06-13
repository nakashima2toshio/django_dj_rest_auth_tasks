# # accounts/views.py
# import logging
# from allauth.account.views import ConfirmEmailView
# # from django.views.generic.base import TemplateResponseMixin
#
# logger = logging.getLogger(__name__)
#
#
# class CustomConfirmEmailView(ConfirmEmailView):
#     # template_name = 'account_confirm_email.html'
#     template_name = "../templates/account/email_confirm.html"  # + app_settings.TEMPLATE_EXTENSION
#     logger.info(template_name)
#
#     def get_template_names(self):
#         # template_name = "../templates/account/email_confirm.html"
#         return ["../templates/account/email_confirm.html"]
