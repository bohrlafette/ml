var express = require('express')
var app = express()

app.use('/css/', express.static('node_modules/bootstrap/dist/css'));
app.use('/js/', express.static('node_modules/bootstrap/dist/js'));

app.use('/js/', express.static('node_modules/jquery/dist'));
app.use('/js/', express.static('node_modules/angular'));
app.use('/js/', express.static('node_modules/angular-resource'));
app.use('/js/', express.static('node_modules/angular-route'));
app.use('/fonts/', express.static('node_modules/bootstrap/dist/fonts'));

app.use('/', express.static('dist'));
 
console.log("Listening on http://localhost:3000");
app.listen(3000)