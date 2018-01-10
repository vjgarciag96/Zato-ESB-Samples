# -*- coding: utf-8 -*-
from zato.server.service import Service
from zato.common import SMTPMessage

class calculator_outgoings_check(Service):

    def send_mail(self, outgoing_name, timestamp):
        self.logger.info('Send mail executing')
        conn = self.email.smtp.get('GMAIL').conn

        msg = SMTPMessage()
        msg.subject = 'Conexión Saliente '+str(outgoing_name)+' caida'
        msg.to = 'vjgarciag96@gmail.com'
        msg.from_ = 'zatoAOS17@gmail.com'
        msg.body = 'La conexión saliente '+str(outgoing_name)+' está caida a fecha de '+str(timestamp)
        conn.send(msg)

    def test_outgoing(self, cid, outgoing, outgoing_name, timestamp):
        try:
            outgoing.conn.ping(cid)
            self.logger.info('Executing try')
        except:
            self.logger.info('Executing except')
            self.send_mail(outgoing_name, timestamp)


    def handle(self):
        add_outgoing = self.outgoing.plain_http.get('Add')
        subtract_outgoing = self.outgoing.plain_http.get('Subtract')
        multiply_outgoing = self.outgoing.soap.get('Multiply')
        divide_outgoing = self.outgoing.plain_http.get('Divide')

        self.test_outgoing(self.cid, add_outgoing, 'Add', self.invocation_time)
        self.test_outgoing(self.cid, subtract_outgoing, 'Subtract', self.invocation_time)
        self.test_outgoing(self.cid, multiply_outgoing, 'Multiply', self.invocation_time)
        self.test_outgoing(self.cid, divide_outgoing, 'Divide', self.invocation_time)


