var express = require('express');
var app = express();
var routes = require('./routes/home') (app);
var bodyParser = require('body-parser');
var methodOverride = require('method-override');

app.set('views', __dirname + '/views/home');
app.set('view engine', 'ejs');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended:true}));
app.use(methodOverride('_method'));
app.engine('html', require('ejs').renderFile);


app.listen(3000, () => {
	console.log('server on! http://localhost:3000');
	app.use(express.static('public'));
});
