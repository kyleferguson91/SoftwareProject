import * as search from "./search.js";
import * as randomplants from "./random-plants.js";


document.addEventListener("DOMContentLoaded", (e) => 
    {
        
        let content = document.querySelector(".contentpane");

        const pages = {
            "My Garden": "/static/pages/my-garden.html",
            "Search for Plants": "/static/pages/search-plants.html",
            "Find Random Plants": "/static/pages/random-plants.html"
        }
      fetch("/static/pages/my-garden.html").then(response => response.text()).then((html) => { content.innerHTML = html}).catch(error => console.error(error));

    let navlist =  document.querySelector(".navlist")        
    navlist.addEventListener('click', (e) =>

                {
                    console.log(e.target.innerText)
                    e.preventDefault()

                    const page = pages[e.target.textContent]

                    if (page)
                    {
                        fetch(page)
                        .then(response => response.text())
                        .then(html => {
                            content.innerHTML = html;

                            
                            if (e.target.innerText.toLowerCase() == "search for plants")
                            {
                                
                                search.searchForPlants();


                            }
                            
                            if (e.target.innerText.toLowerCase() == "find random plants")
                            {
                                randomplants.randomPlants();
                            }


                        })
                        .catch(error => console.error("page loading error: ", error))
                    }

            
                 


            
                    
                
                }


            )
        })

    

    