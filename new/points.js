
let banksDictionary = {"zb bank":"5", "cabs bank":"7", "cbz bank":"9"}


function getPoints() {

    let bankName = document.getElementById('bank-name').value;
    let city = document.getElementById('city-name').value;
    let guuid = banksDictionary[bankName]

    console.log("Found the guuid")
    console.log(guuid)
    url = `https://api-ubt.mukuru.com/taurus/v1/resources/pay-out-partners/${guuid}/locations`
    axios.get(url).then((response) => {console.log(response)})
    
    

    console.log(city)
    console.log(bankName)
    
}