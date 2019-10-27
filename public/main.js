
// const show_screen = {
// 	IDLE: ()=>{ console.log("Showing IDLE")},
// 	INSTRUCTIONS: ()=>{ console.log("Showing INSTRUCTIONS")},
// 	PRE_COUNT: ()=>{ console.log("Showing PRE_COUNT")},
// 	PLAY: ()=>{ console.log("Showing PLAY")},
// 	COUNTDOWN: ()=>{ console.log("Showing COUNTDOWN")},
// 	FINAL: ()=>{ console.log("Showing FINAL")},
// 	system: (com)=> {console.log(com.msg)}

// }

function writeToScreen(val){
	console.log(val)
}

let current_state = "system";

function show_screen(com){
	if (com.state == "system"){
		console.log(com.msg);
		return;
	}

	let time = (current_state != com.state)? 100: 0; 
	current_state = com.state;

	$("#transition").fadeIn( time, ()=> {
		$("#transition").fadeOut(time*2);
		let screens = $(".backplate")
		screens.addClass("hidden");

		// let backplate_id = "#screen_" + com.state;
		let current_screen = $("#screen_" + com.state);
		if (current_screen.length){
			current_screen.removeClass("hidden")
		} else {
			writeToScreen(" *** Not valid state "+ com.state +" ***")
		}
		$("#over p").text(com.count? com.count : "");
	});



}


$( document ).ready(function() {
    console.log( "ready!" );

    const WS_PORT = 8001
    const url = "ws://" + window.location.hostname+":"+ WS_PORT+"/"

    let websocket = new WebSocket(url);
    websocket.binaryType = "arraybuffer";
    websocket.onopen = function(evt) { onOpen(evt) };
    websocket.onclose = function(evt) { onClose(evt) };
    websocket.onmessage = function(evt) { onMessage(evt) };
    websocket.onerror = function(evt) { onError(evt) };





    function onOpen(evt){
      writeToScreen("Client: connected");
      websocket.send("PARI chromium client connected")
    }

    function onClose(evt){
      if (evt.code == 1000){
        writeToScreen("Client: Disconnected");
      } else {
        writeToScreen("Client: Disconnected with error " + evt.code );
        writeToScreen(evt)
      }
    }

    function onMessage(evt){
       try{
          var com =  JSON.parse(evt.data);
	      show_screen(com)
          
          
        } catch (e) {
        	
        	if (e instanceof SyntaxError){
	            writeToScreen("*** Received malformed msg ***");
	            writeToScreen(evt.data)
          	} else {
	            writeToScreen("*** Unknown error ***");
	            console.error(e);
          	}
        }
    	}
      
    function onError(evt){
      var msg = (evt.data)? evt.data : "<no data attached>";
      writeToScreen('Error: ' + msg);
      websocket.close();
      
    }

});