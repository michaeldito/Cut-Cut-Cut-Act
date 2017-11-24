
var restServerAddress = 'http://35.199.191.66/';
$('#result-details-current2018System').slideToggle();
$('#result-details-HouseSystem').slideToggle();

$('#submit').click(function() {
	calcTaxes();
});

$('#showResultDetails2018').click(function() {
	var resultsView = document.getElementById('result-details-current2018System');
	var thisButton = document.getElementById('showResultDetails2018');
	$('#result-details-current2018System').slideToggle();

	if (thisButton.isOpen == 'true') {
		thisButton.isOpen = 'false';
		thisButton.innerHTML = '&#9654';
		console.log('closed twisty');
	}
	else{
		thisButton.isOpen = 'true';
		thisButton.innerHTML = '&#9660';
		console.log('opened twisty');
	}
});

$('#showResultDetailsHouse').click(function() {
	var resultsView = document.getElementById('result-details-HouseSystem');
	var thisButton = document.getElementById('showResultDetailsHouse');
	$('#result-details-HouseSystem').slideToggle();

	if (thisButton.isOpen == 'true') {
		thisButton.isOpen = 'false';
		thisButton.innerHTML = '&#9654';
		console.log('closed twisty');
	}
	else{
		thisButton.isOpen = 'true';
		thisButton.innerHTML = '&#9660';
		console.log('opened twisty');
	}
});

calcTaxes = function() {
	var income = document.getElementById('income').value;
	var status = "";
	var status = $('input[name=status]:checked').val();

	var stateAndLocalTaxDeduction = document.getElementById('stateAndLocalTaxDeduction').value;
	var propertyTaxDeduction = document.getElementById('propertyTaxDeduction').value;
	var medicalExpensesDeduction = document.getElementById('medicalExpensesDeduction').value;
	var tuitionWaved = document.getElementById('tuitionWaved').value;
	var itemizedDeductions = document.getElementById('itemizedDeductions').value;
	var childDependents = document.getElementById('childDependents').value;
	var nonChildDependents = document.getElementById('nonChildDependents').value;

	var postData = {
			income: income,
			status: status,
			stateAndLocalTaxDeduction: stateAndLocalTaxDeduction,
			propertyTaxDeduction: propertyTaxDeduction,
			medicalExpensesDeduction: medicalExpensesDeduction,
			tuitionWaved: tuitionWaved,
			itemizedDeductions: itemizedDeductions,
			childDependents: childDependents,
			nonChildDependents: nonChildDependents
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
		var houseTaxCutsAndJobsActSystem = res.TaxCutsAndJobsActHouse;
		var currentEffectiveTaxRate = ((res.Current2018System.taxedAmountAfterCredits / inputIncome) * 100).toFixed(2);
		var houseEffectiveTaxRate = ((res.TaxCutsAndJobsActHouse.taxedAmountAfterCredits / inputIncome) * 100).toFixed(2);


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

		console.log("         This will be the data sent to the server at resultsView/resultDetails for Current 2018:");
		console.log('            ' + JSON.stringify(current2018TaxSystem));

		$.ajax({
			type: 'POST',
			url: '/resultsView/resultDetails',
			data: JSON.stringify(current2018TaxSystem),
			contentType: 'application/json',
			success: updateResultsSubViewFor2018System,
			error: function(jqXHR, textStatus, errorThrown) {
				console.log("         Error thrown in post to resultsView/resultDetails for Current 2018 in clientController.js, status = " + textStatus);
				console.log("            Error: " + errorThrown);
			}
		});

		console.log("         This will be the data sent to the server at resultsView/resultDetails for the House Tax Cuts and Jobs Act:");
		console.log('            ' + JSON.stringify(houseTaxCutsAndJobsActSystem));

		$.ajax({
			type: 'POST',
			url: '/resultsView/resultDetails',
			data: JSON.stringify(houseTaxCutsAndJobsActSystem),
			contentType: 'application/json',
			success: updateResultsSubViewForHouseTaxCutsAndJobsAct,
			error: function(jqXHR, textStatus, errorThrown) {
				console.log("         Error thrown in post to resultsView/resultDetails for the houseTaxCutsAndJobsActSystem in clientController.js, status = " + textStatus);
				console.log("            Error: " + errorThrown);
			}
		});
	}
	catch(exception) {
		console.log('Caught Exception in clientController/updatePageWithRestServerResponse: ' + exception.message);
	}

}

updateResultsSubViewFor2018System = function(res, status) {
	console.log('         Recieved a succesful response to /resultsView/current2018TaxSystem');
	console.log('         The response is the following:');
	console.log('            ' + res);
	var resultsDiv = document.getElementById('result-details-current2018System');
	resultsDiv.innerHTML = res;
}

updateResultsSubViewForHouseTaxCutsAndJobsAct = function(res, status) {
	console.log('         Recieved a succesful response to /resultsView/current2018TaxSystem');
	console.log('         The response is the following:');
	console.log('            ' + res);
	var resultsDiv = document.getElementById('result-details-HouseSystem');
	resultsDiv.innerHTML = res;
}


function numberWithCommas(x) {
	return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}