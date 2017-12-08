const express = require('express')
const app = express()
const port = 3000

app.get('/', (request, response) => {
  console.log('Hello from Express!')
  response.send('Hello from Express!')
})

app.get('/add', (request, response) => {
  var op1 = parseInt(request.query.op1)
  var op2 = parseInt(request.query.op2)
  var result = op1 + op2
  response.send(String(result))
})

app.listen(port, (err) => {
  if(err) {
    return console.log('something bad happened', err)
  }

  console.log('server is listening on port ' + port)
})
