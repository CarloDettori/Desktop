const width = document.getElementById('inputWidth').value;
const height = document.getElementById('inputHeight').value;

function clickCells() {
     const colorPicker = document.getElementById("colorPicker");
     const cells = document.getElementsByClassName('cell');
     for (let i = 0; i < cells.length; i++) {
         cells[i].addEventListener("click", function (event) {
             let clickedCell = event.target;
             clickedCell.style.backgroundColor = colorPicker.value;
         });
     }
 }

function makeGrid(height, width) {
    const table = document.getElementById("pixelCanvas");
    let grid = '';

    for (let i = 0; i < height; i++) {
        grid += '<tr class="row-' + i + '">';
        for (let j = 0; j < width; j++) {
                grid += '<td class="cell" id="row-' + i + '_cell-' + j + '"></td>';
            }
            grid += '</tr>';
        }
    table.innerHTML = grid;
    addClickEventToCells();
    }

function Submission() {
    event.preventDefault();
    makeGrid(height, width);

document.getElementById('sizePicker').onsubmit = function () {
    Submission();
