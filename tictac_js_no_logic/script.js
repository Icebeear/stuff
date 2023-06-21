arr = document.querySelectorAll("td")

for (var i = 0; i < arr.length; i++) {
    arr[i].addEventListener("click", change)
}

function change() {
    if (this.textContent == "") {
        this.textContent = "X"
    }

    else if (this.textContent == "X") {
        this.textContent = "O"
    }

    else {
        this.textContent = ""
    }
}

function reset() {
    for (i = 0; i < 10; i++) {
        arr[i].textContent = ""
    }
}

btn = document.getElementById("restart")
btn.addEventListener("click", reset)