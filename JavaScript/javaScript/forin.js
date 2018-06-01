
function myfunction(){
    var jsondata =  {fname : "bill", lname : "Gates", age : 65}
    var x;
    var txt = "";
    for (x in jsondata) {
        txt = txt + jsondata[x];
    }
    document.getElementById("demo").innerHTML = txt;
}