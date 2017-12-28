from zato.server.service import Service
from httplib import OK
from json import dumps

class AddServiceAlive(Service):

    def handle(self):
         self.logger.info('Executing...')
         service_outgoing = self.outgoing.plain_http.get('Add')
         try:
            service_outgoing.conn.get(self.cid)
         except:
             out_name = 'Error through ZeroMQ'
             request = {'message' : 'Add outgoing not working!!!'}
             self.outgoing.zmq.send(dumps(request), out_name)


