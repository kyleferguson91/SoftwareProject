
document.addEventListener("DOMContentLoaded", (e) => 
    {
  
        document.querySelectorAll(".nav-button").forEach((e) => 
        {
            e.addEventListener('click', (e) =>
            console.log('clicked' + e.target.textContent)
            )
        })




    })