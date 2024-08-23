let ourClients = []

class User {

    constructor(name, contact, country, birthDay) {
        this.name = name;
        this.contact = contact;
        this.country = country;
        this.birthDay = birthDay;
    }

    toString() {
    return `${this.contact}`;
  }
    
    
}


function addUser() {
    let name = document.getElementById('firstName').value;
    let country = document.getElementById('birthCountry').value;
    let bd = document.getElementById('dob').value;
    let contact = String(document.getElementById('contactDetails').value);
    let myUser = new User(name, contact, country, bd)
    ourClients[ourClients.length] = myUser
    // console.log(userExists(contact))
    window.location.href = 'login.html'

    
}


function userExists(contact) {
    console.log("Length found!! ")
    console.log(contact)

    for(let j = 0; j < ourClients.length; j++) {
        count = 0
        for(let i = 0; i < contact.length; i++) {
            if(ourClients[j].contact.length != contact.length) {continue}
            if(ourClients[j].contact[i] == contact[i]) {count++}
        }
        if(count == contact.length) {
            window.location.href = 'get_points.html'; // send user to different page when successfully logged in
            return true
        }
    }
    return false
}


function landing(event) {
    window.location.href = 'get_points.html'
    event.preventDefault();

    let myVar = document.getElementById("userContact").value;
    console.log(ourClients)
    


    // if(userExists(myVar)) {
    //     console.log("Found")
    //     window.location.href = 'get_points.html'
    // }
    // else {
    //     alert("You are being redirected to the sign up page")


    //     setTimeout(function() {
    //         window.location.href = 'registration.html'; // Change to the desired URL
    //     }, 1000);
        
        
        
        
    //     // window.location.href = 'registration.html'

    // }
    
    
    
}







