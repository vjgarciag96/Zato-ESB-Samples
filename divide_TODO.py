from zato.server.service import Service

class Divide(Service):

    class SimpleIO:
        input_required = ('op1', 'op2')
        output_required = ('result')

    def handle(self):
        try:
            op1 = int(self.request.input.op1)
            #TODO conseguir la variable entera op2 que almacene el valor del operando dos
            #TODO crear variable result con el resultado de la division de op1 y op2
            self.response.payload.result = result
        except:
            self.response.payload.result = "Error"