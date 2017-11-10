
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

	$.post("http://35.203.178.96/cutcutcut", JSON.stringify(postData), function(res, status){
        console.log("results :" + JSON.stringify(res));
        document.getElementById('results').style.visibility = 'visible';
        document.getElementById('tax_results').innerHTML = res.savingsUnderNewPlan;
    }, "json");
}