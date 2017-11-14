var express = require('express');
var router = express.Router();
var calculationController = require('../controllers/calculationController.js');

/* GET home page. */
router.get('/', function(req, res, next) {
	res.render('index', { title: 'Estimate Your Taxes' });
});

/* GET home page. */
router.post('/resultsView/current2018TaxSystem', function(req, res, next) {
	//var tempdata = {'bracketResults' : {'taxedAmountFromBrackets' : 11111}};
	console.log('Recieved request at /resultsView/current2018TaxSystem:');
	console.log('   Request Body:');
	console.log('      Type: ' + typeof(req.body));
	console.log('      ' + JSON.stringify(req.body));
	req.app.render('current2018TaxSystemResults', req.body, function(err, html){
		console.log('zoe is the best!');
		if (err) {
			console.log("Error while rendering current2018TaxSystemResults:")
			console.log('   ' + err);
		}
		else {
			try {
				res.send(html);
			}
			catch(exception) {
				console.log('Cuaght Exception in /resultsView/current2018TaxSystem: ' + exception.message);
			}
		}
	});
});

router.get('/resultsTest', function(req,res,next) {
	req.app.render('current2018TaxSystemResults', function(err, html) {
		console.log("here!");
		res.send(html);
	});
});

router.post('/postTest', function(req, res, next) {
	console.log('recieved hit at postTest');
	return 'testWorks';
});

module.exports = router;
