from zato.server.service import Service

class MyService(Service):
    def handle(self):
        conn = self.email.imap.get('GMAIL').conn

        for msg_id, msg in conn.get():

            # Access the message
            self.logger.info(msg.data)