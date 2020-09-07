console.log(prediction_text)
const p = document.createElement("p");
document.body.appendChild(p);

document.querySelector("form").addEventListener("submit", function(e){

	/*let model_input = ""
	for(i=0; i<12;i++) {
		model_input+=document.querySelectorAll("textarea")[i].value
		model_input+= " "
	}

    p.innerHTML="user entered: " +  model_input;*/
    p.innerHTML = prediction_text;
    e.preventDefault(); 
});