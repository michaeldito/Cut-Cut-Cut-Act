
$('#submit').click(function(){
	calcTaxes();
});

calcTaxes = function() {
	var income = document.getElementById('income').value;
	var status = "";
	if (document.getElementById('single').value != 0) 
		status = "married";
	else
		status = "single";

	var postData = {income: document.getElementById('income').value, status: status}

	$.post("35.203.170.104/cutcutcut", postData.stringify(), function(data, status){
        console.log(status);
    });
}