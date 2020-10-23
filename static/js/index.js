function load() {
    var element = document.getElementById("body");
    console.log(localStorage.getItem('darkmode'))
    if (localStorage.getItem('darkmode')) {
        element.classList.add('dark-mode');
        document.getElementById("darkmode").checked = true;
    }

  document.getElementById("darkmode").addEventListener('change', function () {

        localStorage.setItem('darkmode', this.checked);
        console.log(this.checked)
        if (this.checked) {
            element.classList.add('dark-mode');
            document.getElementById("darkmode").checked = true;
        } else {
            element.classList.remove('dark-mode');
            document.getElementById("darkmode").checked = false;
             localStorage.clear();

        }

    })
}

window.onload = load;
