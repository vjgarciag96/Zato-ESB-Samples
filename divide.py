from zato.server.service import Service

class Divide(Service):

    class SimpleIO:
        input_required = {'op1', 'op2'}
        output_required = {'result'}

    def handle(self):
        try:
            op1 = int(self.request.input.op1)
            op2 = int(self.request.input.op2)
            result = op1/op2
            self.response.payload.result = result
        except:
            self.response.payload.result = """Error"""




