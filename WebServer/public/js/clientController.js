
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

	$.post("/calculate", postData, function(data, status){
        console.log('data: ' + data);
        console.log('status: ' + status);
    }, "json");
}