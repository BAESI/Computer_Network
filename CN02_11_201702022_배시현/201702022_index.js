var express = require('express');
var app = express();
var passport = require('passport');
var session = require('express-session');
var https = require('https');
var fs = require('fs');

var options = {
	key: fs.readFileSync('key.pem'),
	cert: fs.readFileSync('cert.pem')
};

app.set('view engine', 'ejs');
app.use(session({secret:'MySecret',resave: false, saveUninitialized:true}));

//passport setting
app.use(passport.initialize());
app.use(passport.session());

// Routes
app.use('/', require('./routes/main'));
app.use('/auth', require('./routes/auth'));

// Port setting
var port = 3000;
https.createServer(options, app).listen(port, () => {
	console.log('server on! https://localhost:'+port);
});


