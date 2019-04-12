var madlibContainer = document.getElementById("rest_div");
var btn = document.getElementById("btn");
var btn1 = document.getElementById("btn1");
var btn2 = document.getElementById("btn2");
var btn3 = document.getElementById("btn3")

btn.addEventListener("click", function(){
    var ourRequest = new XMLHttpRequest();
    ourRequest.open('GET','http://my-json-server.typicode.com/ktantipa/apple/posts');
    ourRequest.onload = function(){
    var ourData = JSON.parse(ourRequest.responseText);
    renderHTML(ourData);
    };
    ourRequest.send();
});

btn1.addEventListener("click", function(){
    var ourRequest = new XMLHttpRequest();
    ourRequest.open('GET','http://my-json-server.typicode.com/ktantipa/netflex/posts');
    ourRequest.onload = function(){
    var ourData = JSON.parse(ourRequest.responseText);
    renderHTML(ourData);
    };
    ourRequest.send();
});

btn2.addEventListener("click", function(){
    var ourRequest = new XMLHttpRequest();
    ourRequest.open('GET','http://my-json-server.typicode.com/ktantipa/tesla/posts');
    ourRequest.onload = function(){
    var ourData = JSON.parse(ourRequest.responseText);
    renderHTML(ourData);
    };
    ourRequest.send();
});

btn3.addEventListener("click", function(){
    var ourRequest = new XMLHttpRequest();
    ourRequest.open('GET','http://my-json-server.typicode.com/ktantipa/amazon/posts');
    ourRequest.onload = function(){
    var ourData = JSON.parse(ourRequest.responseText);
    renderHTML(ourData);
    };
    ourRequest.send();
});

function renderHTML(data){
    var htmlString = "";

    for (i = 0; i < data.length; i++){
    htmlString += "<li>" + data[i].business_name + " is a " + data[i].business_type + " a company who serves " + data[i].market_type + " customers who needs " + data[i].job_to_be_done + ". We will generate using " + data[i].revenue_model + ".</li>";
        }
madlibContainer.insertAdjacentHTML('beforeend', htmlString);

}


