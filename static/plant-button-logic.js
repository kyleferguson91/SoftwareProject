export function addPlantLogic(plantholder)
{
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
                link: link.href || "No Data",
                id: plantid
                
            };
            let where = "user garden"; // or "user plants"

// now we can pass the appropriate respopnse to the

            if (e.target.classList.contains("add-to-plants"))
            {
                console.log("clicked add to favs, ", plantobj)
                where = "usergarden"
            }

            if (e.target.classList.contains("add-to-garden"))
                {
                    console.log("clicked add to garden, ", plantobj)
                    where = "garden"
                }
    
            fetch("http://127.0.0.1:5000/addplant", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ plantid, plantobj, where })
            })
    
            .catch(error => console.error("Error:", error));
        
            }
    });
    
}