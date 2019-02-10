(function(){

console.log("SEAF Fired")
//save shortcut to button in DOM
var button = document.querySelector("#moreButton");
var eventList = document.querySelector(".eventRow3");

function loadMore() {
	console.log("Click Worked")
	eventList.classList.toggle("slideToggle")

}

button.addEventListener("click", loadMore);

})();

