// import axios from 'axios'

navigator.geolocation.getCurrentPosition((position) => {
    console.log("Lat: ")
    console.log(position.coords.latitude)
    console.log("Long: ")
    console.log(position.coords.longitude)

    
    // doSomething(position.coords.latitude, position.coords.longitude);
  });
  
  
key = "773de069efc30b89839c476356b2799f"
console.log("Printing city...")
res = `http://api.openweathermap.org/geo/1.0/reverse?lat=${-26.150678}&lon=${28.034144}&appid=${key}`
console.log("Cityyyy")
myFunc(res)

function myFunc(res) {
    console.log("Inside")
    axios.get(res).then((response) => {
        console.log(response)
    })

}



// `http://api.openweathermap.org/geo/1.0/reverse?lat=${lat}&lon=${lon}&appid=${key}`