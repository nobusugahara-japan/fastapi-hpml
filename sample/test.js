function exec() {
    console.log("check")
    var elem = document.getElementById("button3");
    var now = new Date();
    var hour = now.getHours();
    var min = now.getMinutes();
    elem.innerHTML = "ボタンがクリックされました。 (" + hour +":" + min + ")";
    
}