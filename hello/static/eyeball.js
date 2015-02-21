
function speakTest(speech)
{

console.log('test alert')
//var gurl= Trim('http://translate.google.com/translate_tts?ie=UTF-8&q='+speech);
console.log(speech);
//console.log(gurl);


document.getElementById('framer').src = 'http://translate.google.com/translate_tts?&tl=en-US&ie=UTF-8&q='+speech;
mouthoff(leng);
//----------------

//---------------
}
// -----------------------------------------------
window.spit_num=0;
function screenSize()
{
window.W=document.body.clientWidth;
window.H=document.body.clientHeight;
}


function spit() {
  console.log('periodic spit:'+String(window.spit_num))
  window.spit_num++;
}
	
	
//   }  ); // end each
  
//   console.log('usernames= '+usernames);
//   console.log('');
//   console.log('screenames= '+screenames);
// 	console.log('this is harvest number: '+harvestNum)
//     //console.log(adata[i].username);
// //for ( var i = 0; i < l; i++ ) {
// //}


// console.log('inside harvestTweets call to tweetstore.json');
 
//  });
 
// }
function setUp() {
  

/* optional checking for html5 file apis, needed to read data
if (window.File && window.FileReader && window.FileList && window.Blob) {
  console.log("Yay - The File APIs are supported by your browser.")
} else {
  console.log('The File APIs are not fully supported by your browser.');
}*/
// +++
$( document ).ready(function() {

// ------------------ adds touch sensitivity -------------
window.addEventListener('load', function(){ // on page load
document.body.addEventListener('touchstart', function(e){
  //keyup();
 }, false)
 }, false)
// ------------------- end touch sensitivity --------------
// window.leng=1;
// window.lock=0; // stop multiple mouth triggers on mouse down
// window.mouthStop=0; // counter needed by swapMouth
// window.mouthNumber=8; // determines how many mouth images can be swapped
// window.faceNum=1; // reference for the folder to look up face image assets in static/images/faces/n/ 
// window.harvestNum=0; // counts how many times the tweetstore has been updated
// speakTest('hello there');
console.log ('Start setUp initialisation...');

window.l= 0;// used later to store array length
// window.usernames = [];
// window.screenames = [];
// loadLastTweet ();

// harvestTweets ();

// +++
console.log ("Hello, Tweetenstein.js...");
try {



// myCanvas.width=W;
// myCanvas.height = H;
// myCanvas2.width=W;
// myCanvas2.height = H;
// var ctxt=document.getElementById("myCanvas");
// window.txt=ctxt.getContext("2d");
// window.fontDef="20px Arial";
// txt.font=fontDef;
// var ctxt2=document.getElementById("myCanvas2");
// window.txt2=ctxt2.getContext("2d");
// window.fontDef2="30px Arial";
// txt2.font=fontDef2;

}
catch (e) { console.log("FAIL"+e)};
}
	);
	console.log('setUp complete!!!');
}
// -------------------------------end setup ---------------------

// speed of text draw
window.phi=100;
// speed of pulse
window.phi2=4000;
window.phi3=3500;

window.txty="Hello World...";

$( document ).ready(function() {
setUp();
});
$( document ).ready(function() {
console.log ('document ready from intervals');
setInterval(function(){spit()}, phi2); // check for changes


});
// window.onkeyup = keyup;

// function keyup()
// {
// window.ran= Math.floor((Math.random()*l)+1);
// console.log ('random number = '+ran)
// console.log('inside keyup detection ');
// window.g='Day-zee. Day-zee. Give me. your answer. do'
// //screenames[ran];
// window.leng=g.length;
// if (window.lock==0) {
// window.lock=1;
// speakTest(g);
//  }
// }
