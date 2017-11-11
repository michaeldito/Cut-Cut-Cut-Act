
$('#submit').click(function(){
	calcTaxes();
});

calcTaxes = function() {
	var income = document.getElementById('income').value;
	var status = "";
	if (document.getElementById('single').value != 0) 
		status = "single";
	else
		status = "married";

	var postData = {
			income: document.getElementById('income').value,
			status: status,
			deductions: 0,
			stateAndLocalTaxDeduction: 6000,
			credits: 0,
			personalExemptions: 1
	}

	console.log("postData: " + JSON.stringify(postData));

	$.ajax({
		type: "POST",
		url: "http://35.203.158.17/cutcutcut",
		data: JSON.stringify(postData),
		success: function(res, status) {
			try {
				console.log('recieved a response');
				console.log("results :" + JSON.stringify(res));
				document.getElementById('results').style.visibility = 'visible';
				document.getElementById('tax_results').innerHTML = res.savingsUnderNewPlan;
			}
			catch(exception) {
				console.log('Caught Exception: ' + e.message);
			}
    	},
		error: function(jqXHR, textStatus, errorThrown) {
			alert("Error, status = " + textStatus + ", " +
				"error thrown: " + errorThrown);
		}
	});
}