
import * as random from "./random-plants.js"

let index = 0;
export function populatePlants(response)
{
    console.log(response)
    let holder = document.querySelector(".plantbox")
    for (let e of response["plants"])
    {
        console.log(e)
        //create a new div for each plant

        let plantentry = document.createElement("div")
        plantentry.classList.add("plantentry");
        
        //create image holder
        let image = document.createElement("img")
        image.classList.add("plantitemimage")
        //update source to supplied info
        image.src=e.images.thumb

        //create name div
        let namediv = document.createElement("div")
        namediv.classList.add("namediv")



        //create name holder
        let name = document.createElement("p")
        name.classList.add("plantitemname")
        name.textContent = e.name

        let type = document.createElement("p")
        type.classList.add("plantitemname")
        type.textContent = e.type


        namediv.appendChild(name)
        //then append type to namediv
        namediv.appendChild(type)
        
           //more info button
           let moreinfolink = document.createElement("a")
               moreinfolink.target="_blank"
           moreinfolink.href="https://permapeople.org/"+e.link
            
           moreinfolink.textContent="Click for more info"
      

           namediv.appendChild(moreinfolink)

        //append properties to each entry div
        plantentry.appendChild(namediv)
        plantentry.appendChild(image)
        
        let infodiv = document.createElement("div")
            infodiv.classList.add("infodiv")
            infodiv.classList.add("infodiv1")
              //infodiv #2
              let infodiv2 = document.createElement("div")
              infodiv2.classList.add("infodiv")
              infodiv2.classList.add("infodiv2")
  

        for (let i = 0; i<e.data.length; i++)
        {
           
                console.log(e.data[i].key)
                if (e.data[i].key == "Light requirement" || e.data[i].key == "Water requirement" || e.data[i].key == "Soil type"
                    || e.data[i].key == "Height" || e.data[i].key == "Width"
                    
                )
                {
                    console.log(e.data[i].key + " " + e.data[i].value)
                    let key = document.createElement("p")
                    key.classList.add("infodivtitle")
                    key.textContent = e.data[i].key || "no data"
                    let info = document.createElement("p")
                    info.classList.add("infodivinfotitle")
                    info.id = (e.data[i].key.split(" ").join("").toLowerCase())
                    info.textContent = e.data[i].value || "no data"
                    
                    infodiv.appendChild(key)
                    infodiv.appendChild(info)

                 
                    //we only want to apply the id parameter once
                    //we will put this onto our button objects that are on each plant



                }

            }
            //append info div to entry
            plantentry.appendChild(infodiv)

      for (let i = 0; i<e.data.length; i++)
        {
           
                console.log(e.data[i].key)
                if (e.data[i].key == "Layer" || e.data[i].key == "Life cycle" || e.data[i].key == "Edible"
                    || e.data[i].key == "Growth" || e.data[i].key == "Edible parts"
                )
                {
                    console.log(e.data[i].key + " " + e.data[i].value)
                    let key = document.createElement("p")
                    key.classList.add("infodivtitle")
                    key.textContent = e.data[i].key+" " || "no data"
                    let info = document.createElement("p")
                    info.classList.add("infodivinfotitle")
                    info.id = (e.data[i].key.split(" ").join("").toLowerCase())
                    info.textContent = e.data[i].value.charAt(0).toUpperCase() + e.data[i].value.substring(1)  || "no data"
                    infodiv2.appendChild(key)
                    infodiv2.appendChild(info)



                    //apply to infodiv 2
                    

                }

            }
      



           plantentry.appendChild(infodiv2)
           let addtogarden = document.createElement("button")
           let addtoplants = document.createElement("button")
 
           addtoplants.classList.add("add-to-plants")
           addtoplants.innerHTML = "Add to my Plants"

           addtogarden.classList.add("add-to-garden")
           addtogarden.innerHTML = "Add to my garden"

            let buttonholder = document.createElement("div")
            buttonholder.classList.add("button-holder")

            addtogarden.id = e.id
            addtoplants.id = e.id

            buttonholder.appendChild(addtoplants)
            buttonholder.appendChild(addtogarden)
            plantentry.appendChild(buttonholder)

            // we will look to adding database functions here, mainly buttons to start that call other functions
            //ensure we grab the plant id when passing the data which will allow us to determine other info
            //another loop again for each plant for a new pane that contains the buttons? 

            

         


        //append the div to the main holder
        holder.appendChild(plantentry);




    }

    //AFTER POPULATED WE CAN ADD A CLICK TO EACH OF OUR BUTTONS
    let plantholder = document.querySelector(".plantbox")
    plantholder.addEventListener("click", (e) => {
        if (e.target.tagName == "BUTTON") {
            let plantid = e.target.id;
            let parent = e.target.closest(".plantentry");
            let info = parent.querySelector(".infodiv1")
            let info2 = parent.querySelector(".infodiv2")
            let water = parent.querySelector("#waterrequirement") || "No data"
            let light = parent.querySelector("#lightrequirement") || "No data"
            let soil = parent.querySelector("#soiltype") || "No data"
            let height = parent.querySelector("#height") || "No data"
            let edible = parent.querySelector("#edible") || "No data"
            let growth = parent.querySelector("#growth") || "No data"
            let layer= parent.querySelector("#layer") || "No data"
            let edibleparts = parent.querySelector("#edibleparts") || "No data"
            let link = parent.querySelector("a") || "No data"
            console.log(water.innerText, light.innerText, soil.innerText, height.innerText, edible.innerText, growth.innerText,
                layer.innerText, edibleparts.innerText
            )
            //extract the info from the relevant areas
            let plantobj = {
                water: water.innerText || "No Data",
                light: light.innerText || "No Data",
                soil: soil.innerText || "No Data",
                height: height.innerText || "No Data",
                edible: edible.innerText || "No Data",
                growth: growth.innerText || "No Data",
                layer: layer.innerText || "No Data",
                edibleparts: edibleparts.innerText || "No Data",
                link: link.href || "No Data"
            };
            let where = "user garden"; // or "user plants"

// now we can pass the appropriate respopnse to the backend

            if (e.target.classList.contains("add-to-plants"))
            {
                console.log("clicked add to favs, ", plantobj)
            }

            if (e.target.classList.contains("add-to-garden"))
                {
                    console.log("clicked add to garden, ", plantobj)
                }
    /*
            fetch("http://127.0.0.1:5000/addplant", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ plantid, plantobj, where })
            })
            .then(response => response.json())
            .then(data => console.log("Response from Python:", data))
            .catch(error => console.error("Error:", error));
        */
            }
    });


    /*
// add a button to bottom to get the next 100 results

    let nextbutton = document.createElement("button")
    nextbutton.textContent = "Show me more!"
    

    nextbutton.addEventListener('click', (e) => 
    {

        //on button click we want to call populate plants again, with a new response and a new link
        console.log('nextutton clicked give be more')

        //get a new response with last id = 100 (index = 100)
        //increment by 100 each time
        index=index+100

        random.moreRandomPlants(index)
        //now we increment index by 100


    })


    holder.appendChild(nextbutton);

*/


}




