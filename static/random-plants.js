import * as populate from "./populate-plants.js"
export function randomPlants(index) {

    console.log('random plant search stuff here')

    document.querySelector(".findrandomplantbutton").addEventListener('click', (e) => {
        console.log('find random button clicked call endpoint and log')

        let randomURL = `http://127.0.0.1:5000/randomplants?lastid=${index}`;


        fetch(randomURL)
            .then(response => response.json())
            .then(response => (populate.populatePlants(response)))
            .catch(error => console.error("Error fetching data:", error));

    
    })




}


export function moreRandomPlants(index) {

        console.log("more random plants")
        console.log("index of more random plants is " + index)
    
        let randomURL = `http://127.0.0.1:5000/randomplants?lastid=${index}`;

        console.log("more random url is " + randomURL)
        fetch(randomURL)
            .then(response => response.json())
            .then(response => console.log)
            .then(response => (populate.populatePlants(response)))
            .catch(error => console.error("Error fetching data:", error));

    
    




}