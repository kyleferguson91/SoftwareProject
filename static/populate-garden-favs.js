export function populateGardenFavs(where)
{
    console.log("popgardenfavs", "where is equal to ", where)
    fetch('http://127.0.0.1:5000/populatefavsgarden', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({where})
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));


    //get a response from python backend via database

}