console.log('test');


//create event to load on dom content loaded


document.addEventListener("DOMContentLoaded", (e) => 
{

//down arrow functionality

let downarrow = document.querySelector(".downarrow")
let entrypage = document.querySelector(".entrypage")

// disappear on click
downarrow.addEventListener("click", (e) => {

    entrypage.classList.add("hidden");

})

//disappear on scroll

document.addEventListener("scroll", (e) => {
    entrypage.classList.add("hidden");
    


})





})