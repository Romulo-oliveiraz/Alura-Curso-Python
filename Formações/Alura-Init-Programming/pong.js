let xball = 300;
let yball = 200;
let zball = 50;

let xballSpeed = 6;
let yballSpeed = 6;

let radio = zball / 2;


let xrect = 10
let xrect2 = 580
let yrect = 150
let yrect2 = 150
let heigth_rect = 10
let width_rect = 90

let radiorect = width_rect / 2;


function setup() {
  createCanvas(600, 400);
}

function draw() {
  background(0);
  showball();
  ballmoviment();
  ballcolision();
  show_rects();
  rect1_moviment()
}

function showball(){
  circle(xball,yball,zball);
}

function show_rects(){
  rect(xrect, yrect, heigth_rect, width_rect);
  rect(xrect2, yrect2, heigth_rect, width_rect);
}

function rect1_moviment(){
  if (keyIsDown(UP_ARROW) && width_rect < height){
    yrect -= 10
  }
  if (keyIsDown(DOWN_ARROW)){
    yrect += 10
  }
}

function ballmoviment(){
  xball += xballSpeed;
  yball += yballSpeed;
}

function ballcolision(){
  if (xball + radio > width || xball - radio < 0){
    xballSpeed *= -1;
  }
  if (yball + radio > height || yball - radio < 0){
    yballSpeed *= -1;
  }
}