
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
	var stateAndLocalTaxDeduction = document.getElementById('stateAndLocalTaxDeduction').value;
	var deductions = document.getElementById('deductions').value;
	var credits = document.getElementById('credits').value;
	var personalExemptions = document.getElementById('personalExemptions').value;

	var postData = {
			income: document.getElementById('income').value,
			status: status,
			deductions: deductions,
			stateAndLocalTaxDeduction: stateAndLocalTaxDeduction,
			credits: credits,
			personalExemptions: personalExemptions
	}

	console.log("postData: " + JSON.stringify(postData));

	$.ajax({
		type: "POST",
		url: "http://35.203.158.17/cutcutcut",
		data: JSON.stringify(postData),
		success: function(res, status) {
			try {
				console.log("results :" + JSON.stringify(res));
				
				var summaryMessage = document.getElementById('tax_results')
				var percentSavingsMessage = document.getElementById('tax_results_percent')
				var dollarSavings = Math.round(res.savingsUnderNewPlan * 100) / 100
				var inputIncome = document.getElementById('income').value;
				var percentSavings = Math.abs(((dollarSavings / inputIncome) * 100).toFixed(2))


				document.getElementById('results').style.visibility = 'visible';
				if (dollarSavings < 0)
					dollarSavings *= -1;

				if (res.savingsUnderNewPlan > 0) {
					summaryMessage.innerHTML = "You will pay $" + dollarSavings.toFixed(2) + " less in taxes under the proposed house bill.";
					summaryMessage.style.color = 'green';
					percentSavingsMessage.innerHTML = "This is " + percentSavings + "% of your income";
					percentSavingsMessage.style.color = 'green';
				}
				else {
					summaryMessage.innerHTML = "You will pay $" + dollarSavings.toFixed(2) + " more in taxes under the proposed house bill.";
					summaryMessage.style.color = 'red';
					percentSavingsMessage.innerHTML = "This is " + percentSavings + "% of your income";
					percentSavingsMessage.style.color = 'red';
				}


			}
			catch(exception) {
				console.log('Caught Exception: ' + exception.message);
			}
    	},
		error: function(jqXHR, textStatus, errorThrown) {
			alert("Error, status = " + textStatus + ", " +
				"error thrown: " + errorThrown);
		}
	});
}