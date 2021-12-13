var slider = document.getElementById("bright");
var output = document.getElementById("value");

slider.oninput = function() {
	output.innerHTML = this.value;
}
