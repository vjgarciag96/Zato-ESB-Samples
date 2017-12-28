# -*- coding: utf-8 -*-

from zato.common import SMTPMessage
from zato.server.service import Service

class SendEmailService(Service):
    def handle(self):

        # Obtain a connection
        conn = self.email.smtp.get('GMAIL').conn

        # Create a regular e-mail
        msg = SMTPMessage()
        msg.subject = 'Hello'
        msg.to = 'vjgarciag96@gmail.com'
        msg.from_ = 'zatoAOS17@gmail.com'
        msg.body = 'El servicio Add se ha quedado moñeco!! Salu2 :D'

        # Send the message
        conn.send(msg)