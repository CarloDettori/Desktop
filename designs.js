let width = document.getElementById('inputWidth').value;
let height = document.getElementById('inputHeight').value;
const submitt = document.getElementById('submitting').value;
let desingText = document.getElementById('pixelCanvas').value;


function clickCells() {
     const colorPicker = document.getElementById("colorPicker").value;
     const cells = document.getElementsByClassName('cell');
     for (let i = 0; i < cells.length; i++) {
         cells[i].addEventListener("click", function (event) {
             let clickedCell = event.target;
             clickedCell.style.backgroundColor = colorPicker;
         });
     }
 }


function makeGrid(height, width) {
    const table = document.getElementById("pixelCanvas");
    let grid = '';
    for (let i = 0; i < height; i++) {
        for (let j = 0; j < width; j++) {
            let newCell = document.createElement("div");
            j.appendChild(newCell) = "cell";
            }
        }
    table.innerHTML = grid;
    addClickEventToCells();
    }
submitt.addEventListener('click', function () {
    console.log('The heading was clicked!');


    function Submission() {
        event.preventDefault();
        makeGrid(height, width);
    };



