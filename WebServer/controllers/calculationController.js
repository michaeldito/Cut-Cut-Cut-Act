


var calculateTaxes = function (req, res, next) {
	console.log('found the function');
	console.log(req.body);
	var data = req.body;
	console.log('income: ' + data.income);
	console.log('status: ' + data.status);
	
	$.post("35.203.164.77/cutcutcut", data, function(res, status){
        console.log(res);
        console.log(response);
    }, "json");
}


module.exports.calculateTaxes = calculateTaxes;