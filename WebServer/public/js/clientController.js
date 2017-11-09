
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
			status: status
		}

	console.log(JSON.stringify(postData));

/*
	$.post("/calculate", postData, function(data, status){
        console.log('data: ' + data);
        console.log('status: ' + status);
    }, "json");
*/

	$.post("http://35.203.178.96/cutcutcut", JSON.stringify(postData), function(res, status){
        console.log("process :" + JSON.stringify(res));
        document.getElementById('results').style.visibility = 'visible';
        document.getElementById('tax_results').innerHTML = res.tax;
    }, "json");
}