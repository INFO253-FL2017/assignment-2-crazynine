var commentForm = document.getElementById("commentForm");
var result = document.getElementById("result");
var temp = "";
commentForm.addEventListener("submit", function(event) {;
	name = commentForm.elements.namedItem("name").value;
	message = commentForm.elements.namedItem("message").value;
	var result = document.getElementById("result");
	localStorage.setItem(name, name);
	localStorage.setItem(message, message);
	if(localStorage.getItem("forever2") != null) {
		temp = localStorage.getItem("forever2");
	}
	temp = temp + name + ": " + message + "<br />";

	localStorage.setItem("forever2", temp);
	result.innerHTML = localStorage.getItem("forever2");

	event.preventDefault();
})

result.innerHTML = localStorage.getItem("forever2");
