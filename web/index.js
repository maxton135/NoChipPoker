
// Profile Image Changing

const profileImgs = ["Fish", "Basic Fish", "Sexy Fish", "Fish Fish", "Thicc Fish", "Shark"]
var player1img = 0;
var player2img = 0;
var player3img, player4img, player5img = 0;

const profileButtons = document.querySelectorAll(".profile-img-btn");
console.log(profileButtons);

profileButtons.forEach(btn => {
    btn.addEventListener('click', ev => {
        const clicked = ev.target.id;
        if (clicked == "player1-img-right")
          $('#player1-img').html = profileImgs[(++player1img) % 5];
        else if (clicked == "player1-img-left")
            document.getElementById('player1-img').innerHTML = profileImgs[(--player1img) % 5];
    })
})

// Profile Name Fetching

const readyButtons = document.querySelectorAll(".ready-btn");

readyButtons.forEach(btn => {
    btn.addEventListener('click', ev => {
        const clicked = ev.target.id;
        if (clicked == "player1-btn") {
            
        }
    })
})
console.log(readyButtons);