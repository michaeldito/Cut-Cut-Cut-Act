
$('#submit').click(function(){
	calcTaxes();
});

calcTaxes = function() {
	var income = document.getElementById('income').value;
	var status = "";
	var status = $('input[name=status]:checked').val();
	console.log('status ' + status);

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
				//console.log("results :" + JSON.stringify(res));
				
				var summaryMessage = document.getElementById('tax_results')
				var percentSavingsMessage = document.getElementById('tax_results_percent')
				var dollarSavings = Math.round(res.savingsUnderNewPlan * 100) / 100
				var inputIncome = document.getElementById('income').value;
				var percentSavings = Math.abs(((dollarSavings / inputIncome) * 100).toFixed(2));
				var current2018TaxSystem = res.Current2018System;
				var currentEffectiveTaxRate = ((res.Current2018System.taxedAmountAfterCredits / inputIncome) * 100).toFixed(2);
				var houseEffectiveTaxRate = ((res.TaxCutsAndJobsActHouse.taxedAmountAfterCredits / inputIncome) * 100).toFixed(2);

				console.log('Type: ' + typeof(current2018TaxSystem));

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

				console.log("This will be the data sent to the server at resultsView/current2018TaxSystem:");
				console.log('   ' + JSON.stringify(current2018TaxSystem));

				$.ajax({
					type: 'POST',
					url: '/resultsView/current2018TaxSystem',
					data: JSON.stringify(current2018TaxSystem),
					dataType: 'json',
					success: function(res, status) {
						var resultsDiv = document.getElementById('result-details-current2018System');
						console.log('status of results 2018 query' + status);
						console.log('res of results 2018 query' + res);
						resultsDiv.innerHTML = res;
					},
					error: function(jqXHR, textStatus, errorThrown) {
						alert("Error thrown in post to resultsView/current2018TaxSystem in clientController.js, status = " + textStatus + ", " +
							"error thrown: " + errorThrown);
					}
				});

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