"use strict";
function asteroids() {
    const svg = document.getElementById("canvas");
    const playerScore = new Elem(svg, "text")
        .attr("x", 20)
        .attr("y", 50)
        .attr("font-size", 50)
        .attr("fill", "#FFFF33");
    let g = new Elem(svg, 'g')
        .attr("transform", "translate(300 300) rotate(170)");
    let ship = new Elem(svg, 'polygon', g.elem)
        .attr("points", "-15,20 15,20 0,-20")
        .attr("style", "fill:lime;stroke:purple;stroke-width:1");
    const shipState = {
        x: 300,
        y: 300,
        shipRotation: 170,
        r: 20,
        checkGotHit: 0,
        score: 0
    };
    const mainInterval = Observable.interval(10);
    mainInterval.subscribe(() => {
        g.attr("transform", "translate(" + shipState.x + " " + shipState.y + ") rotate(" + shipState.shipRotation + ")"),
            playerScore.elem.textContent = String(shipState.score);
    });
    let asteroids = new Array();
    Observable.interval(100)
        .subscribe(() => {
        if (asteroids.length < 8) {
            asteroids.push(new Elem(svg, "circle")
                .attr("cx", Number(Math.floor(Math.random() * 600)))
                .attr("cy", Number(Math.floor(Math.random() * 600)))
                .attr("angle", Number(Math.floor(Math.random() * 180)))
                .attr("r", 50)
                .attr("checkGotHit", 0)
                .attr("fill", "#FFC0CB")
                .attr("xSpeed", 10)
                .attr("ySpeed", 10));
        }
        bullets.map(b => {
            console.log(asteroids);
            asteroids.map(a => checkIfHitAsteroid(b, a));
        });
        asteroids.map((a) => {
            if (a.attr("checkGotHit") == String(0) || a.attr("checkGotHit") == String(2)) {
                let aX = Number(a.attr("cx"));
                let aAngle = Number(a.attr("angle"));
                aX += Math.cos(aAngle * Math.PI / 180 - Math.PI / 2) * 2;
                if (aX < svg.clientLeft) {
                    aX = svg.clientWidth;
                }
                else if (aX > svg.clientWidth) {
                    aX = svg.clientLeft;
                }
                a.attr("cx", aX);
                let aY = Number(a.attr("cy"));
                aY += Math.sin(aAngle * Math.PI / 180 - Math.PI / 2) * 2;
                if (aY > svg.clientHeight) {
                    aY = svg.clientTop;
                }
                else if (aY < svg.clientTop) {
                    aY = svg.clientHeight;
                }
                a.attr("cy", aY);
            }
            else if (a.attr("checkGotHit") == String(1)) {
                a.attr("checkGotHit", 3);
                asteroids.push(new Elem(svg, "circle")
                    .attr("cx", Number(a.attr("cx")))
                    .attr("cy", Number(a.attr("cy")))
                    .attr("angle", Number(Math.floor(Math.random() * 180)))
                    .attr("r", 20)
                    .attr("checkGotHit", 2)
                    .attr("fill", "#ADD8E6")
                    .attr("xSpeed", 10)
                    .attr("ySpeed", 10));
                asteroids.push(new Elem(svg, "circle")
                    .attr("cx", Number(a.attr("cx")))
                    .attr("cy", Number(a.attr("cy")))
                    .attr("angle", Number(Math.floor(Math.random() * 180)))
                    .attr("r", 20)
                    .attr("checkGotHit", 2)
                    .attr("fill", "#ADD8E6")
                    .attr("xSpeed", 10)
                    .attr("ySpeed", 10));
            }
        });
        bullets.map(b => {
            let bX = Number(b.attr("cx"));
            let bAngle = Number(b.attr("angle"));
            bX += Math.cos(bAngle * Math.PI / 180 - Math.PI / 2) * 5;
            b.attr("cx", bX);
            let bY = Number(b.attr("cy"));
            bY += Math.sin(bAngle * Math.PI / 180 - Math.PI / 2) * 5;
            b.attr("cy", bY);
        });
        asteroids.map(a => checkIfHitShip(a));
    });
    const keydown = Observable.fromEvent(document, 'keydown');
    const keyup = Observable.fromEvent(document, 'keyup');
    keydown
        .filter(key => key.keyCode == 65)
        .subscribe(() => shipState.shipRotation -= 5);
    keydown
        .filter(key => key.keyCode == 68)
        .subscribe(() => shipState.shipRotation += 5);
    keydown
        .filter(key => key.keyCode == 87)
        .subscribe(() => moveShip());
    function moveShip() {
        shipState.x += Math.cos(shipState.shipRotation * Math.PI / 180 - Math.PI / 2) * 5;
        if (shipState.x < svg.clientLeft) {
            shipState.x = svg.clientWidth;
        }
        else if (shipState.x > svg.clientWidth) {
            shipState.x = svg.clientLeft;
        }
        shipState.y += Math.sin(shipState.shipRotation * Math.PI / 180 - Math.PI / 2) * 5;
        if (shipState.y > svg.clientHeight) {
            shipState.y = svg.clientTop;
        }
        else if (shipState.y < svg.clientTop) {
            shipState.y = svg.clientHeight;
        }
    }
    let bullets = new Array();
    keydown
        .filter(key => key.keyCode == 32)
        .subscribe(() => bullets.push(new Elem(svg, "circle")
        .attr("cx", shipState.x)
        .attr("cy", shipState.y)
        .attr("angle", shipState.shipRotation)
        .attr("r", 5)
        .attr("fill", "#FF0000")
        .attr("xSpeed", 10)
        .attr("ySpeed", 10)));
    function checkIfHitAsteroid(a, b) {
        let aRadius = Number(a.attr("r"));
        let bRadius = Number(b.attr('r'));
        let betweenX = Number(b.attr("cx")) - Number(a.attr("cx"));
        let betweenY = Number(b.attr("cy")) - Number(a.attr("cy"));
        let betweenCentre = Math.sqrt((betweenX * betweenX) + (betweenY * betweenY));
        if (betweenCentre <= aRadius + bRadius) {
            if (b.attr("r") == String(50) && b.attr("checkGotHit") == String(0)) {
                shipState.score += 5;
            }
            else if (b.attr("r") == String(20) && b.attr("checkGotHit") == String(2)) {
                shipState.score += 10;
            }
            let hitCheck = Number(b.attr("checkGotHit"));
            hitCheck += 1;
            b.attr("checkGotHit", hitCheck);
            b.elem.remove();
        }
    }
    function checkIfHitShip(a) {
        let aRadius = Number(a.attr("r"));
        let shipRadius = Number(shipState.r);
        let betweenX = Number(shipState.x) - Number(a.attr("cx"));
        let betweenY = Number(shipState.y) - Number(a.attr("cy"));
        let betweenCentre = Math.sqrt((betweenX * betweenX) + (betweenY * betweenY));
        if (betweenCentre <= aRadius + shipRadius && a.attr("checkGotHit") != String(3)) {
            let hitCheck = Number(shipState.checkGotHit);
            hitCheck += 1;
            shipState.checkGotHit = hitCheck;
            ship.elem.remove();
        }
    }
}
if (typeof window != 'undefined')
    window.onload = () => {
        asteroids();
    };
//# sourceMappingURL=asteroids.js.map