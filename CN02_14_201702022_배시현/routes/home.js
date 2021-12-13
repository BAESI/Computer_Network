var express =require('express');
var router = express.Router();

router.get('/', (req, res) => {
	res.render('hue_controller');
});

var Hue = require('philips-hue');
var hue = new Hue();

hue.bridge = "";
hue.username = "";

router.post('/huecontrol', (req, res) => {
	const id = req.body.hueid
	const power = req.body.power
	var state = {bri: Number(req.body.brightness),sat: Number(req.body.saturation),hue: Number(req.body.hue)}
	try {
		if ( power == "On") {
				hue.light(id).on().then(console.log).catch(console.error);
				hue.light(id).setState(state).then(console.log).catch(console.error);
			}
			else {
				hue.light(id).off().then(console.log).catch(console.error);
			}
	}catch (error){
		console.error(error);
	}
	res.render('hue_controller');
});

module.exports = router;
