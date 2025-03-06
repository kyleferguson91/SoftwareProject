export function populateGardenFavs(where)
{
    console.log("popgardenfavs", "where is equal to ", where)
    fetch('http://127.0.0.1:5000/populatefavsgarden', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        mode:'cors',
        body: JSON.stringify({where})

    })
    .then(response => response.json())
    .then(data => populateGUI(data))
    .catch(error => console.error('Error:', error));


    //get a response from python backend via database
    
}

function populateGUI(data)
{
console.log(data)
let parent = document.querySelector(".cardplantdisplay")
// now we have json data here!
for (let key in data) {
    if (data.hasOwnProperty(key)) {
      if (key === 'plants') {  
        data[key].forEach(plant => {  

       
        // now we have all the info here, we want to populate the display with relevant info
        let name = plant.name
        let link = plant.link
        let soil = plant.soil
        let light = plant.light
        let water = plant.water
        let layer = plant.layer
        let height = plant.height
        let growth = plant.growth
        let edibleparts = plant.edibleparts
        let edible = plant.edible
        let imagelink = plant.imagelink

            let info = `${imagelink} ${name} ${link} ${soil} ${light} ${water} ${layer} ${height} ${growth} ${edible} ${edibleparts} `
          console.log(info);  
          console.log(parent)

          let plantcard = document.createElement("div")
          plantcard.classList.add("plantcard")


          let plantimageholder = document.createElement("div")
          plantimageholder.classList.add("cardimageholder")

          let image = document.createElement("img")
          image.classList.add("galleryplantimage")
        
          image.src=imagelink

          let plantname = document.createElement("p")
          plantname.classList.add("plantname")
          plantname.innerText = name
          
          plantimageholder.appendChild(plantname)
          plantimageholder.appendChild(image)
        
          let moreinfo = document.createElement("a")
          moreinfo.href = link
          moreinfo.innerText = "More Info"
          moreinfo.target="_blank"
          plantimageholder.appendChild(moreinfo)

         

          plantcard.appendChild(plantimageholder)   

          parent.appendChild(plantcard)

          let infobox = document.createElement("div");
          infobox.classList.add("cardinfobox")


          // loop for this stuff ? 
          //traverse this plant
          for (let key in plant)
          {
            if (key == "growth" || key == "water" || key == "soil" || key == "light" || key == "height")
            {
                console.log(plant[key])

                //create a title div
                let title = document.createElement("p")
                //set inner text to the key value
                title.innerText = key.substring(0,1).toUpperCase() + key.substring(1)
                title.classList.add("cardinfotitle")
                //attach title to the infobox
                
                infobox.appendChild(title)

                //attach the value next
                let valuebox = document.createElement("p")
                valuebox.innerText = plant[key]
                valuebox.classList.add("cardinfotext")
                infobox.appendChild(valuebox)
                

            }
          }
          let removePlant = document.createElement("button")
          removePlant.innerText = "Remove Plant"
          removePlant.classList.add("remove-plant-btn")
          infobox.appendChild(removePlant)

           

          //lightinfo






          plantcard.appendChild(infobox)


        });
      }
    }


}

}