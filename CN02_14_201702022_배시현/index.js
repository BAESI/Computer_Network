var express = require('express');
var bodyParser = require('body-parser');
var methodOverride = require('method-override');
var app = express();
var path = require('path');

app.set('view engine', 'jade');
app.set('views', './views');
app.use(express.static(path.join(__dirname, '/')));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended:true}));
app.use(methodOverride('_method'));

app.use('/', require('./routes/home'));

app.listen(3000, () => {
	console.log('server on! http://localhost:3000');
});
