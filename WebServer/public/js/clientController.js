
var restServerAddress = 'http://35.203.158.17/';

$('#submit').click(function() {
	calcTaxes();
});

calcTaxes = function() {
	var income = document.getElementById('income').value;
	var status = "";
	var status = $('input[name=status]:checked').val();

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

	console.log("Sending data to Rest Server /cutcutcut: ");
	console.log('   ' + JSON.stringify(postData));
	console.log();

	sendDataToRestServerAndUpdatePage(postData);

}

sendDataToRestServerAndUpdatePage = function(postData) {
	$.ajax({
		type: "POST",
		url: restServerAddress + 'cutcutcut',
		data: JSON.stringify(postData),
		success: updatePageWithRestServerResponse,
		error: function(jqXHR, textStatus, errorThrown) {
			console.log("   Error thrown in post to Rest Server /cutcutcut in clientController.js, status = " + textStatus);
			console.log("      Error: " + errorThrown);
		}
	});
}

updatePageWithRestServerResponse = function(res, status) {
	try {
		console.log('   Recieved successful response from Rest Server');
		console.log('      The response is the following:');
		console.log('         ' + JSON.stringify(res));
		
		var summaryMessage = document.getElementById('tax_results');
		var percentSavingsMessage = document.getElementById('tax_results_percent');
		var dollarSavings = Math.round(res.savingsUnderNewPlan * 100) / 100;
		var inputIncome = document.getElementById('income').value;
		var percentSavings = Math.abs(((dollarSavings / inputIncome) * 100).toFixed(2));
		var current2018TaxSystem = res.Current2018System;
		var currentEffectiveTaxRate = ((res.Current2018System.taxedAmountAfterCredits / inputIncome) * 100).toFixed(2);
		var houseEffectiveTaxRate = ((res.TaxCutsAndJobsActHouse.taxedAmountAfterCredits / inputIncome) * 100).toFixed(2);

		console.log('Type: ' + typeof(current2018TaxSystem));

		document.getElementById('results').style.visibility = 'visible';
		if (dollarSavings < 0)
			dollarSavings *= -1;

		dollarSavingsText = numberWithCommas(dollarSavings.toFixed(2));

		if (res.savingsUnderNewPlan > 0) {
			summaryMessage.innerHTML = "You will pay $" + dollarSavingsText + " less in taxes under the proposed house bill.";
			summaryMessage.style.color = 'green';
			percentSavingsMessage.innerHTML = "This is " + percentSavings + "% of your income";
			percentSavingsMessage.style.color = 'green';
		}
		else {
			summaryMessage.innerHTML = "You will pay $" + dollarSavingsText + " more in taxes under the proposed house bill.";
			summaryMessage.style.color = 'red';
			percentSavingsMessage.innerHTML = "This is " + percentSavings + "% of your income";
			percentSavingsMessage.style.color = 'red';
		}

		console.log("         This will be the data sent to the server at resultsView/current2018TaxSystem:");
		console.log('            ' + JSON.stringify(current2018TaxSystem));

		$.ajax({
			type: 'POST',
			url: '/resultsView/current2018TaxSystem',
			data: JSON.stringify(current2018TaxSystem),
			contentType: 'application/json',
			success: updateResultsSubViewFor2018System,
			error: function(jqXHR, textStatus, errorThrown) {
				console.log("         Error thrown in post to resultsView/current2018TaxSystem in clientController.js, status = " + textStatus);
				console.log("            Error: " + errorThrown);
			}
		});
	}
	catch(exception) {
		console.log('Caught Exception: ' + exception.message);
	}

}

updateResultsSubViewFor2018System = function(res, status) {
	console.log('         Recieved a succesful response to /resultsView/current2018TaxSystem');
	console.log('         The response is the following:');
	console.log('            ' + res);
	var resultsDiv = document.getElementById('result-details-current2018System');
	resultsDiv.innerHTML = res;
}


function numberWithCommas(x) {
	return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}