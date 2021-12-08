const table = document.getElementById("pixel_canvas");
const sizePicker = document.getElementById("sizePicker");
const colorPicker = document.getElementById("colorPicker");


sizePicker.addEventListener('submit', function() {
    let width = document.getElementById("input_width").value;
    let height = document.getElementById("input_height").value;
    makeGrid(width, height);
  })

  function makeGrid(width, height) {
    table.innerHTML = '';
    for (let cell= 0; cell < height; cell++ ) {
        let newCell = newRow.insertCell();
            for (let row = 0; row < width; row++) {
                let newRow = table.insertRow();
                newCell.onclick = changeColor;
        }
    }
  }

  function changeColor() {
    style.background = colorPicker.value;
  }
