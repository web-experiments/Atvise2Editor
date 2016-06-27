/*
Test ob alles richtig eingebaut wird
*/
var test = "AGENT.OBJECTS.Test"
webMI.data.subscribe(test,function(e){
    console.log("Wert:" + e.value)
})


var sI = setInterval(function(){
    webMI.data.read(test,function(e){
        if(e.value) {
            webMI.data.write("AGENT.OBJECTS.Test",false)
        } else {
            webMI.data.write("AGENT.OBJECTS.Test",true);
        }
    })
},50)