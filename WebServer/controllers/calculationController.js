var $ = require('jquery');

var calculateTaxes = function (req, res, next) {
	console.log('found the function');
	console.log(req.body);
	var data = req.body;
	console.log('income: ' + data.income);
	console.log('status: ' + data.status);
	
	$.post("35.203.178.96/cutcutcut", JSON.stringify(data), function(res, status){
        console.log("process :" + res);
    }, "json");
}


module.exports.calculateTaxes = calculateTaxes;