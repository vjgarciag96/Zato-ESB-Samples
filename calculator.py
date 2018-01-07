from __future__ import absolute_import, division, print_function, unicode_literals
from zato.server.service import Service
import json

class Calculator(Service):

    ADD_CODE = 1
    SUBTRACT_CODE = 2
    MULTIPLY_CODE = 3
    DIVIDE_CODE = 4

    class SimpleIO:
        input_required = {'code', 'op1', 'op2'}
        output_required = {'result'}

    def add(self, cid, op1, op2):
        params = {}
        params['op1'] = op1
        params['op2'] = op2
        add = self.outgoing.plain_http.get('Add')
        response = add.conn.get(cid, params)
        return response.content

    def subtract(self, cid, op1, op2):
        params = {}
        params['op1'] = op1
        params['op2'] = op2
        subtract = self.outgoing.plain_http.get('Subtract')
        response = subtract.conn.get(cid, params)
        return response.content

    def multiply(self, cid, op1, op2):
        with self.outgoing.soap.get('Multiply').conn.client() as client:
            arg1 = int(op1)
            arg2 = int(op2)
            return client.service.multiply(arg1, arg2)

    def divide(self, cid, op1, op2):
        params = {}
        params['op1'] = op1
        params['op2'] = op2
        divide = self.outgoing.plain_http.get('Divide')
        response = divide.conn.get(cid, params)
        return json.loads(response.content)['response']['result']


    def handle(self):
        options = {self.ADD_CODE: self.add,
                   self.SUBTRACT_CODE: self.subtract,
                   self.MULTIPLY_CODE: self.multiply,
                   self.DIVIDE_CODE: self.divide}
        code = int(self.request.input.code)
        self.response.headers['Access-Control-Allow-Origin'] = '*'
        self.response.payload.result = options[code](self.cid, self.request.input.op1, self.request.input.op2)


