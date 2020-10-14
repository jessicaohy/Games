// Jessica Oh Hui Yu 29886465
// FIT2102 2019 Assignment 1
// https://docs.google.com/document/d/1Gr-M6LTU-tfm4yabqZWJYg-zTjEVqHKKTCvePGCYsUA/edit?usp=sharing

////////////////////////////// DETAILS ON DESIGN ///////////////////////////////
// The state of the ship is kept. The attributes added are radius, check if the ship is hit and score.
// This way, it is able to get the ship attributes and they can be changed.
// The score is created using svg as a new text element instead of using HTML as this will allow the score to be on the canvas instead of being on top of the canvas.

// Using Observable, a main interval loop is created and it runs every 10 milliseconds.
// The ship's movements and updating of the player's score is subscribed to this loop.

// For the ship to be able to rotate and move, the transform property is changed using the ship's x and y coordinates, and its angle.
// Using Observable, the document will check whether the keys are pressed down.
// The Observable is filtered to check what key is being pressed down and actions are subscribed to it.
// When the player presses the keys a and d, the ship's angle are decremented and incremented respectively.
// When the player presses key w, the x and y coordinates are calculated.
// The x and y coordinates calculated are checked whether it exceeds the canvas boundaries. 
// If it is, it will wrap around the canvas by assigning it to the opposite side of the canvas.
// When the player presses the key space, bullets are created ,using the ship's x and y coordinates so that it will appear from the ship's position, and put into an array.
// The bullet's angle and movement are similar to moving the ship but is given random movement.

// Using Oberservable, another interval loop is created and it runs every 100 milliseconds. 
// This is created for the asteroids and bullets to have a slower reaction compared to the ship.
// Creation of asteroids and movements of asteroids and bullets are subscribed to this interval.
// An array is created to contain the asteroids created. Asteroids are created until the asteroids array has a length of 10.

// Every asteroids and bullets are checked to see if they collide with each other.
// This is done by creating a reusable function that uses Pythagoras Theorem to calculate if the asteroid and bullet are close together.
// When the bullets hit the big asteroid, the big asteroid's attribute, checkGotHit, will change to 1.
// This means that the big asteroid has to be removed and 2 smaller asteroids have to be created.
// These 2 smaller asteroids' checkGotHit will be set to 2.
// When the bullets hit the small asteroid, the small asteroid will siappear and its attribute, checkHotHit, will change to 3. 
// Having different values for the attributes enable different conditions to be met and allow different actions to be controlled based on whether the asteroids are alive or not.
// If the attribute, checkGotHit is 0 or 2, the asteroids can move around the canvas.
// When the asteroids hit the ship, the ship will be removed and the game ends.

// When the asteroid is destroyed, its radius will be checked.
// If the destroyed asteroid is big, the ship's score will increase by 5.
// If the small asteroid is destroyed, the ship's score will increase by 10.
// The score will be updated on the canvas.

////////////////////////////////////////////////////////////////////////////////

function asteroids() {
  // Inside this function you will use the classes and functions 
  // defined in svgelement.ts and observable.ts
  // to add visuals to the svg element in asteroids.html, animate them, and make them interactive.
  // Study and complete the Observable tasks in the week 4 tutorial worksheet first to get ideas.

  // You will be marked on your functional programming style
  // as well as the functionality that you implement.
  // Document your code!  
  // Explain which ideas you have used ideas from the lectures to 
  // create reusable, generic functions.

  const svg = document.getElementById("canvas")!;

  // TO DISPLAY PLAYER SCORE
  const playerScore = new Elem(svg, "text")
    .attr("x", 20)
    .attr("y", 50)
    .attr("font-size", 50)
    .attr("fill", "#FFFF33")  // yellow

  //////// CREATING SHIP //////////
  // make a group for the spaceship and a transform to move it and rotate it
  // to animate the spaceship you will update the transform property
  let g = new Elem(svg,'g')
    .attr("transform", "translate(300 300) rotate(170)")
  
  // create a polygon shape for the space ship as a child of the transform group
  let ship = new Elem(svg, 'polygon', g.elem) 
    .attr("points","-15,20 15,20 0,-20") //"-15,20 15,20 0,-20"
    .attr("style","fill:lime;stroke:purple;stroke-width:1")
    //.attr("r", 30) // added for calculation
    //.attr("checkGotHit", 0)
  
  const shipState = {
    x: 300,
    y: 300,
    shipRotation: 170,                // angle of the ship
    r: 20,                            // radius of the ship, treat it as circle to calculate collision
    checkGotHit: 0,
    score: 0                          // player's score to display on the svg
  }

  // MAIN GAME LOOP. SUBSCRIBES EVERY 10 MILLISECONDS.
  const mainInterval = Observable.interval(10)
  mainInterval.subscribe(() => {g.attr("transform","translate("+shipState.x+" "+shipState.y+") rotate("+shipState.shipRotation+")"),
                                playerScore.elem.textContent = String(shipState.score)
                                })
  
  // ANOTHER INTERVAL FOR ASTEROIDS AND BULLETS
  let asteroids = new Array<Elem>();  // array containing many asteroids

  // setInterval(() => { // same as observable 
  Observable.interval(100)
    .subscribe(() => {                           
    // CREATING ASTEROIDS
    if (asteroids.length < 8){ // make sure it only creates 8
      asteroids.push(new Elem(svg, "circle")
      .attr("cx", Number(Math.floor(Math.random()*600)))        // created at random places
      .attr("cy", Number(Math.floor(Math.random()*600)))
      .attr("angle", Number(Math.floor(Math.random()*180)))     // move random directions
      .attr("r", 50)
      .attr("checkGotHit", 0)
      .attr("fill", "#FFC0CB") // pink
      .attr("xSpeed", 10)
      .attr("ySpeed", 10))
    }

    // Before moving asteroids, check if it is dead.
    // If it is dead, make sure it cannot move or do anything and disappear from the screen
    // svg.elem.remove to hide from the screen

    // CHECK IF BULLET HIT ASTEROID
    bullets.map(b => {
      console.log(asteroids) 
      asteroids.map(a => 
      checkIfHitAsteroid(b, a))
    })

    // for every asteroid, change x and y to move
    asteroids.map((a) => {
      // Before moving asteroids, check if it is dead.
      // 0 = big asteroid alive
      // 1 = big asteroid needs to split into 2 small asteroids
      // 2 = small asteroid alive
      // 3 = dead

      // MOVE ASTEROIDS
      if (a.attr("checkGotHit") == String(0) || a.attr("checkGotHit") == String(2)){ // did not get hit
      // need to wrap around canvas (if go to much to one side, come out from opposite side)
      //x coordinates
      let aX = Number(a.attr("cx"));
      let aAngle = Number(a.attr("angle"));
      aX += Math.cos(aAngle*Math.PI/180 -Math.PI/2) *2
      if (aX < svg.clientLeft){             // if all the way to the left
        aX = svg.clientWidth                // put it to the right
      }
      else if (aX > svg.clientWidth){       // if all the way to the right
        aX = svg.clientLeft                 // put it to the left
      }
      a.attr("cx", aX)                      // update

      // y coordinates
      let aY = Number(a.attr("cy"))
      aY += Math.sin(aAngle*Math.PI/180 -Math.PI/2) *2
      if (aY > svg.clientHeight){           // if all the way below
        aY = svg.clientTop                  // put it to the top
      }
      else if (aY < svg.clientTop){         // if all the way above
        aY = svg.clientHeight               // put it to the bottom
      }
      a.attr("cy", aY)                      // update
      }

      else if (a.attr("checkGotHit") == String(1)){ // if hit big asteroids
        // make big asteroid dead
        // let hitCheck = Number(a.attr("checkGotHit"))
        // hitCheck = 3
        a.attr("checkGotHit", 3)

        // CREATE 2 SMALL ASTEROIDS
        asteroids.push(new Elem(svg, "circle") 
        .attr("cx", Number(a.attr("cx"))) // create from the dead big asteroid
        .attr("cy", Number(a.attr("cy")))
        .attr("angle", Number(Math.floor(Math.random()*180)))
        .attr("r", 20)
        .attr("checkGotHit", 2)
        .attr("fill", "#ADD8E6") // blue
        .attr("xSpeed", 10)
        .attr("ySpeed", 10))

        asteroids.push(new Elem(svg, "circle") 
        .attr("cx", Number(a.attr("cx"))) // create from the dead big asteroid
        .attr("cy", Number(a.attr("cy")))
        .attr("angle", Number(Math.floor(Math.random()*180)))
        .attr("r", 20)
        .attr("checkGotHit", 2)
        .attr("fill", "#ADD8E6") // blue
        .attr("xSpeed", 10)
        .attr("ySpeed", 10))

      }
    })

    // MOVE BULLETS
    bullets.map(b => {
      // do not need to wrap
      //x coordinates
      let bX = Number(b.attr("cx"));
      let bAngle = Number(b.attr("angle"));
      bX += Math.cos(bAngle*Math.PI/180 -Math.PI/2) *5
      b.attr("cx", bX)      // update

      // y coordinates
      let bY = Number(b.attr("cy"))
      bY += Math.sin(bAngle*Math.PI/180 -Math.PI/2) *5
      b.attr("cy", bY)      // update
    })

  // SHIP GOT SHOT AND DIED
  asteroids.map(a => checkIfHitShip(a))
  })
  // }, 100)
  
  const keydown = Observable.fromEvent<KeyboardEvent>(document, 'keydown')
  const keyup = Observable.fromEvent<KeyboardEvent>(document, 'keyup')

  ///////// ROTATE SHIP ////////
    // moving get ship position and direction and update them
  // w =  step on gas, a and d = rotates, space = shoot

  // rotate ship left
  keydown
    .filter(key => key.keyCode == 65) // a
    .subscribe(() => shipState.shipRotation-=5)

  // rotate ship right
  keydown
    .filter(key => key.keyCode == 68) // d
    .subscribe(() => shipState.shipRotation+=5)

  ////// MOVE SHIP ////////
  // move ship
  keydown
    .filter(key => key.keyCode == 87) //  w
    .subscribe(() => moveShip())

  // calculate x and y coordinates to move ship
  function moveShip(){
    // integer division, multiply substract
    // if greater than this return this
    // wrap x coordinate
    // before assigning, wrap in ternery or if else

    // x coordinates
    shipState.x+= Math.cos(shipState.shipRotation*Math.PI/180 -Math.PI/2) *5
    if (shipState.x < svg.clientLeft){              // if go too much to the left
      shipState.x = svg.clientWidth                 // put it to the right
    }
    else if (shipState.x > svg.clientWidth){        // if go too much to the right
      shipState.x = svg.clientLeft                  // put it to the left
    }
    // y coordinates
    shipState.y+= Math.sin(shipState.shipRotation*Math.PI/180 -Math.PI/2) *5
    if (shipState.y > svg.clientHeight){            // if go too much to the bottom
      shipState.y = svg.clientTop                   // put it to the top
    }
    else if (shipState.y < svg.clientTop){          // if go too much to the top
      shipState.y = svg.clientHeight                // put it to the bottom
    }
  }

  ///////// SHOOTING //////////
  // CREATE BULLETS 
  let bullets = new Array<Elem>();
  keydown
    .filter(key => key.keyCode == 32) // space
    .subscribe(() =>
      bullets.push(new Elem(svg, "circle")      
      .attr("cx", shipState.x)
      .attr("cy", shipState.y)
      .attr("angle", shipState.shipRotation)
      .attr("r", 5)
      .attr("fill", "#FF0000") // red
      .attr("xSpeed", 10)
      .attr("ySpeed", 10))
    )
  
  // calculate if hit opponent
  function checkIfHitAsteroid(a: Elem, b: Elem){   // checkIfHit(shooter, victim)
    // console.log("check")
    let aRadius = Number(a.attr("r"))
    let bRadius = Number(b.attr('r'))

    let betweenX = Number(b.attr("cx")) - Number(a.attr("cx"))
    let betweenY = Number(b.attr("cy")) - Number(a.attr("cy"))
    let betweenCentre = Math.sqrt((betweenX*betweenX) + (betweenY*betweenY))

    if (betweenCentre <= aRadius + bRadius){
      
      // increase player score
      if (b.attr("r") == String(50) && b.attr("checkGotHit") == String(0)){ // big asteroid
        shipState.score += 5 // increase player score

      }
      else if (b.attr("r") == String(20) && b.attr("checkGotHit") == String(2)){ // small asteroid
        shipState.score += 10 // increase player score

      }
      let hitCheck = Number(b.attr("checkGotHit"))
      hitCheck += 1
      b.attr("checkGotHit", hitCheck)
      b.elem.remove() // remove ASTEROID from display
      
    }
    
  }

  // calculate if hit ship
  function checkIfHitShip(a: Elem){
    let aRadius = Number(a.attr("r"))
    let shipRadius = Number(shipState.r)

    let betweenX = Number(shipState.x) - Number(a.attr("cx"))
    let betweenY = Number(shipState.y) - Number(a.attr("cy"))
    let betweenCentre = Math.sqrt((betweenX*betweenX) + (betweenY*betweenY))

    if (betweenCentre <= aRadius + shipRadius && a.attr("checkGotHit") != String(3)){   // make sure asteroid is not dead
      let hitCheck = Number(shipState.checkGotHit)
      hitCheck += 1
      shipState.checkGotHit = hitCheck
      ship.elem.remove() // remove SHIP from display
    }
  }

}

// the following simply runs your asteroids function on window load.  Make sure to leave it in place.
if (typeof window != 'undefined')
  window.onload = ()=>{
    asteroids();
  }

 