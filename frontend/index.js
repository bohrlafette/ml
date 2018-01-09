var express = require('express')
var proxy = require('http-proxy-middleware');
var app = express()

app.use('/css/', express.static('node_modules/bootstrap/dist/css'));
app.use('/css/', express.static('node_modules/font-awesome/css'));
app.use('/js/', express.static('node_modules/bootstrap/dist/js'));

app.use('/lib/', express.static('node_modules/angular-ui-bootstrap/dist'));

app.use('/js/', express.static('node_modules/jquery/dist'));
app.use('/js/', express.static('node_modules/angular'));
app.use('/js/', express.static('node_modules/angular-animate'));
app.use('/js/', express.static('node_modules/angular-resource'));
app.use('/js/', express.static('node_modules/angular-route'));
app.use('/fonts/', express.static('node_modules/bootstrap/dist/fonts'));
app.use('/fonts/', express.static('node_modules/font-awesome/fonts'));

app.use('/', express.static('dist'));

app.use('/api', proxy({target: 'http://localhost:5000', changeOrigin: true, pathRewrite: {'^/api/' : '/'}}));
 
console.log("Listening on http://localhost:3000");
app.listen(3000)