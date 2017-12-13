var express = require('express')
var app = express()

app.use('/css/', express.static('node_modules/bootstrap/dist/css'));
app.use('/js/', express.static('node_modules/bootstrap/dist/js'));
app.use('/fonts/', express.static('node_modules/bootstrap/dist/fonts'));

app.use('/', express.static('src'));
 
app.listen(3000)