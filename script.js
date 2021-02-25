var heading;
var buttons = document.getElementsByClassName('colourButton');
var answerMessage = document.getElementById('answer');
var R, G, B;

heading = document.getElementById('colourValue');

function makeColourValue(){
  return Math.round(Math.random() * 255);
}

function setButtonColour(button, r, g, b){
  button.setAttribute('style',
                      'background-color: rgb(' + r + ',' + g + ','+ b +');'
                      );
}

function startGame() {
  
  var answer = Math.round(Math.random() * (buttons.length - 1));
  setButtonColour(body, 255, 255, 255);
  answerMessage.innerHTML = "";
  
for (var i = 0 ; i < buttons.length; ++i) {
  var r = makeColourValue();
  var g = makeColourValue();
  var b = makeColourValue();
  setButtonColour(buttons[i], r, g, b);
  
  if (i === answer) {
    R = r;
    G = g;
    B = b;
    heading.innerHTML = `(${r},${g},${b})`;
  }

  buttons[i].addEventListener('click', function(){
    if (this === buttons[answer]) {
      answerMessage.innerHTML = "정답!";
      setButtonColour(body, R, G, B);
    } else {
      answerMessage.innerHTML = "땡!";
    }
  });
}
}

startGame();

document.getElementById('resetButton').addEventListener('click', startGame);

