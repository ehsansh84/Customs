__author__ = 'Adel'

import mandrill

class SendMail:

    __mandrill_client = mandrill.Mandrill('XDi4Hai25FOo_dUX1lwSTQ')
#-----------------------------------------------------------------------------------------------------------------------

    @classmethod
    def send_email_welcome(cls, subject, email_address, from_name, from_email, dynamic_vars_list):
        message = {
            'subject': subject,
            'to': [{'email': email_address}],
            'from_name': from_name,
            'from_email': from_email,
            'track_opens': True, 'track_clicks': False,
            'global_merge_vars':  [{'name': 'FNAME', 'content': dynamic_vars_list[0]},
                                   {'name': 'LNAME', 'content': dynamic_vars_list[1]},
                                   {'name': 'UPARAM', 'content': dynamic_vars_list[2]}]
        }
        cls.__mandrill_client.messages.send_template(template_name="welcome_template", template_content=[], message=message)
        return
#-----------------------------------------------------------------------------------------------------------------------

    @classmethod
    def contactus_send_to_admin(cls, subject, email_address, from_name, from_email, dynamic_vars_list):
        message = {
            'subject': "via Republishan contact us page - " + subject,
            'to': [{'email': email_address}],
            'from_name': from_name,
            'from_email': from_email,
            'track_opens': True, 'track_clicks': False,
            'global_merge_vars':  [{'name': 'NAME', 'content': dynamic_vars_list[0]},
                                   {'name': 'MESSAGE', 'content': dynamic_vars_list[1]}]
        }
        cls.__mandrill_client.messages.send_template(template_name="contactus_admin", template_content=[], message=message)
        return
#-----------------------------------------------------------------------------------------------------------------------

    @classmethod
    def contactus_back_to_user(cls, subject, email_address, from_name, from_email, dynamic_vars_list):
        message = {
            'subject': subject,
            'to': [{'email': email_address }],
            'from_name': from_name,
            'from_email': from_email,
            'track_opens': True, 'track_clicks': False,
            'global_merge_vars':  [{'name': 'NAME', 'content': dynamic_vars_list[0]}]
        }
        cls.__mandrill_client.messages.send_template(template_name="contactus_user", template_content=[], message=message)
        return
#-----------------------------------------------------------------------------------------------------------------------

