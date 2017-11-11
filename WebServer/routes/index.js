var express = require('express');
var router = express.Router();
var calculationController = require('../controllers/calculationController.js');

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Estimate Your Taxes' });
});

router.post('/postTest', function(req, res, next) {
	console.log('recieved hit at postTest');
	return 'testWorks';
});

module.exports = router;
