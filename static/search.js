import { populatePlants } from "./populate-plants.js"

export function searchForPlants()
{
    let submit = document.querySelector("#searchform")
    let input = document.querySelector(".searchinput")

    submit.addEventListener("submit", (e) => 
    {
        e.preventDefault()
        console.log(input.value)  

        //now we have user input

        //we want to fetch the results from the api and for now return json
        //we should use a new function to perform this 

        //
        searchAPI(input.value.toString())
    })





}


function searchAPI(query)
{

let searchUrl = `http://127.0.0.1:5000/search?q=${query}`;
//clear the screen for the new search results!
let plantbox = document.querySelector(".plantbox")
plantbox.innerHTML = "";


fetch(searchUrl)
.then(response => response.json())
.then(response => populatePlants(response))
.catch(error => console.error("Error fetching data:", error));
}


