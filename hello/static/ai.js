
function speakTest(speech)
{

console.log('test alert')
//var gurl= Trim('http://translate.google.com/translate_tts?ie=UTF-8&q='+speech);
console.log(speech);
//console.log(gurl);
document.getElementById('framer').src = 'http://translate.google.com/translate_tts?&tl=en-US&ie=UTF-8&q='+speech;
mouthoff(leng);
}
function randomName ()
{
window.ran= Math.floor((Math.random()*l)+1);
console.log ('random number = '+ran);
console.log ('random HHHHHHHHHHHHHHHHHHHHHHnumber = '+ran);
console.log('inside keyup detection ');
window.g=screenames[ran];
window.leng=g.length;
}
function sentenceMaker1(len) // generates sentences (wow, really?!) of length 'len'
{
window.sentence='';   //window.g+'. ';
window.sen=window.sentence;
window.wchk=0;
window.threer=0; // this randomises if text or names are used
while (wchk<len) {
if (window.threer==0) {
window.wran= Math.floor((Math.random()*window.wlen));
//window.wranCHK=wran;
sen=sen+' '+wordies[wran];

window.wchk++;
}
} // end while
window.sentence=sen;
//mouthoff(leng);
}

function sentenceMaker2(len) // generates sentences (wow, really?!) of length 'len'
{
plen=window.phrases.length;
console.log ("plen= "+plen);
window.randPhrase = window.phrases[Math.floor(Math.random() *plen )];
window.sentence=randPhrase;//window.phrases[2];   //window.g+'. ';
sen=window.sentence;
window.wchk=0;
window.threer=0; // this randomises if text or names are used
while (wchk<len) {
window.threer= Math.floor((Math.random()*6));
if (window.threer!=0) {
window.wran= Math.floor((Math.random()*window.wlen));
sen=sen+' '+wordies[wran];
wran=wran+1;
// sen=sen+'. ';
if (window.wranCHK<window.wlen)
{
sen=sen+' '+wordies[wran+1];
} 

window.wchk++;
}
if (window.threer==0) {
randomName();
sen=sen+window.g;
window.wchk++;
}
} // end while
window.sentence=sen;
//mouthoff(leng);
}


function speakSentence(sentence)
{

console.log('test alert')
//var gurl= Trim('http://translate.google.com/translate_tts?ie=UTF-8&q='+speech);
console.log('Sentence= '+sentence);
//console.log(gurl);
document.getElementById('framer').src = 'http://translate.google.com/translate_tts?&tl=en-US&ie=UTF-8&q='+sentence;
mouthoff(leng);
}

function screenSize()
{
window.W=document.body.clientWidth;
window.H=document.body.clientHeight;
}
//-------------------------------Set Up------------------------
function yep() {
 console.log ('yep');
}
function loadLastTweet ()
{
$.getJSON( "lastTweet.json", function( data ) {
 console.log('start lastTweet');
  //console.log(data.lasttweetID);
  window.lasttweetID=data.lasttweetID;
  console.log(lasttweetID);
  console.log('Success from inside getJson call to lastTweet.json');
 });
}

function swapMouth(le)
{

console.log ('le- '+le)
console.log ('mouthStop = '+mouthStop);
if (le > mouthStop)
{
console.log('if is working'); 
window.ran2= Math.floor((Math.random()*mouthNumber)+1);
console.log ('random number = '+ran2)
//console.log(leng);
imger = 'images/faces/'+faceNum+'/MOUTH-'+ran2+'.jpg';
window.mouthy.src=imger;
mouthStop+=1;
} else { 
console.log('if ELSE is working ');
mouthStop=0; // reset timer
clearInterval(gobo)
window.lock=0; //reset lock variable
}
console.log('inside swapMouth');


}
function mouthoff(le)
{
window.mouthTimer=80;
window.gobo = setInterval(function(){swapMouth(le)},mouthTimer); //redraws a backgound to make the text visible
//swapMouth(le);
}
function harvestTweets ()
{
while(usernames.length > 0) {
    usernames.pop();
}
console.log('usernames reset');

while(screenames.length > 0) {
    screenames.pop();
}
console.log('screenames reset');
harvestNum++;
console.log('start harvestTweets');

$.getJSON( "tweetstore2.json", function(adata) {
console.log('l = '+adata.store.length);
l=adata.store.length; // set max 'l' based on length of imported array

$.each( adata.store, function(key,val) {
	//console.log('key= '+key,val.username,val.screen_name);
	usernames.push (val.username);
	screenames.push (val.screen_name)

  }  ); // end each
  
  
  // -------------
  
  
 $.get('words.txt', function(wdata) {
    window.wordies = wdata.split(',');
	window.wlen=window.wordies.length
	console.log('window.wordies.length= '+window.wordies.length);
	
	console.log('wordies= '+wordies [1]);
});


  
  
  //-----------------------
  
  
  console.log('usernames= '+usernames);
  console.log('');
  console.log('screenames= '+screenames);
	console.log('this is harvest number: '+harvestNum)
    //console.log(adata[i].username);
//for ( var i = 0; i < l; i++ ) {
//}


console.log('inside harvestTweets call to tweetstore.json');
 
 });
 
}
function setUp() {

/* optional checking for html5 file apis, needed to read data
if (window.File && window.FileReader && window.FileList && window.Blob) {
  console.log("Yay - The File APIs are supported by your browser.")
} else {
  console.log('The File APIs are not fully supported by your browser.');
}*/
// +++
$( document ).ready(function() {
window.wran=0; // used to access words from array
window.phrases=[".Perhaps you might",".Is it really true", ".Don't assume always that", ".Have you pondered", ".Try something different like" , ".Maybe its", ".You might like", ".Grasp the" , ".Believe in a" , ".How you feel about" , ".Something unexpected like", ".Unexpected issues may", ".What could go wrong with" ]
console.log ("phrases length = "+phrases.length);
window.leng=1;
window.lock=0; // stop multiple mouth triggers on mouse down
window.mouthStop=0; // counter needed by swapMouth
window.mouthNumber=8; // determines how many mouth images can be swapped
window.faceNum=1; // reference for the folder to look up face image assets in images/faces/n/ 
window.harvestNum=0; // counts how many times the tweetstore has been updated
speakTest('..Hello there! Newcastle! Rock and Roll');
//mouthoff(5);
console.log ('Start setUp initialisation...');

window.l= 0;// used later to store array length
window.usernames = [];
window.screenames = [];
loadLastTweet ();

harvestTweets ();

// +++
console.log ("Hello, Tweetenstein.js...");
try {



myCanvas.width=W;
myCanvas.height = H;
myCanvas2.width=W;
myCanvas2.height = H;
var ctxt=document.getElementById("myCanvas");
window.txt=ctxt.getContext("2d");
window.fontDef="20px Arial";
txt.font=fontDef;
var ctxt2=document.getElementById("myCanvas2");
window.txt2=ctxt2.getContext("2d");
window.fontDef2="30px Arial";
txt2.font=fontDef2;

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
console.log ('document ready from intervals');
setInterval(function(){harvestTweets()}, phi2); // check for changes


});
window.onkeyup = function keyup()
{
event = event || window.event;
window.kee=window.event.keyCode
console.log ('>>>>>>>>>>>>>>>>>>>>>>>event.keyCode= '+kee);
// spacebar actions
if (kee==32){

randomName();
if (window.lock==0) {
window.lock=1;
speakTest(g);
 }
 } // end spacebar
 
 // left arrow actions
if (kee==37){
randomName();
if (window.lock==0) {
window.lock=1;
speakTest(g);
 }
} // end left arrows

 // right arrow actions
if (kee==39){
randomName();
if (window.lock==0) {
window.lock=1;
speakTest(g);
 }
} // end right arrows


// up arrow
if (kee==38){
sentenceMaker1(10);
randomName();
window.leng=window.sentence.length;
if (window.lock==0) {
window.lock=1;
speakSentence(window.sentence);
 }
} // end up arrows

 // down arrow actions
if (kee==40){
sentenceMaker2(10);
randomName();
window.leng=window.sentence.length;
if (window.lock==0) {
window.lock=1;
speakTest(window.sentence);
 }
} // end down arrows

} // end of key up >>>

$( document ).ready(function() {
setUp();
});