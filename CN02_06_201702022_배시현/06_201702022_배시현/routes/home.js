module.exports =function(app)
{
	app.get('/',function(req,res) {
		res.render('welcome.ejs')
	});
	app.get('/about',function(req,res) {
		res.render('about.ejs');
	});
}
