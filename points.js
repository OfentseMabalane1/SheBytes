let banks = []
let banksDictionary = {"zb bank":"5", "cabs bank":"7", "cbz bank":"9"}


function getPoints(event) {
    event.preventDefault()

    let bankName = document.getElementById('bank-name').value;
    let city = document.getElementById('city-name').value;
    let guuid = banksDictionary[bankName]

    console.log("Found the guuid")
    console.log(guuid)
    url = `https://api-ubt.mukuru.com/taurus/v1/resources/pay-out-partners/${guuid}/locations`
    // axios.get(url).then((response) => {console.log(response)})

    fetch(url)
    .then(data => {
        let myVar = data.json()
        myVar.then(data => {
            storeBanks(data.items, city)})
    })
    
}


function storeBanks(listOfBanks, userCity) {
    console.log(listOfBanks)

    for(let i = 0; i < listOfBanks.length; i++) {
        banks[i] = listOfBanks[i]
    }

    console.log(banks)
}