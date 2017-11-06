var express = require('express');
var router = express.Router();
var calculationController = require('../controllers/calculationController.js');

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.post('/calculate', function(req, res, next) {
	console.log('here')
    calculationController.calculateTaxes(req, res, next);
});

module.exports = router;
