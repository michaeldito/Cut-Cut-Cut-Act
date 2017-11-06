
var calculateTaxes = function (req, res, next) {
	console.log('found the function');
	console.log(req.body);
	var data = req.body;
	console.log('income: ' + data.income);
	console.log('status: ' + data.status);
}


module.exports.calculateTaxes = calculateTaxes;