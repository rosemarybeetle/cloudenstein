var mention_text;
var datetime;
function fill_foam()
{
var wordy = document.getElementById("entry").value;
  document.getElementById("foam").innerHTML+='inside fill_framer - passed argument = '+wordy; 

}

function getDate()
{
  var currentdate = new Date(); 
datetime = "Last Sync: " + currentdate.getDate() + "/";
datetime += (currentdate.getMonth()+1)  + "/";
datetime += currentdate.getFullYear() + " @ ";
datetime += currentdate.getHours() + ":";
datetime += currentdate.getMinutes() + ":" ;
datetime += currentdate.getSeconds();
}
function mentions() 
  {
    $.getJSON( "http://cloudenstein.rosemarybeetle.org/recent_mentions", function(mens) {
try {
  var cont=mens.count;
  if (cont>0){
    mention_text=''; // clear mention_text

  for ( var i = 0; i < cont; i++ ) {
    getDate();
mention_text=datetime+': - New mention number '+String(i)+ 'with id:'+mens.mentions[i].status_id+' from user: @'+mens.mentions[i].screen_name+'('+mens.mentions[i].name+').<br />';
document.getElementById("foam").innerHTML+=mention_text;
  console.log('username '+String(i)+ '= '+mens.mentions[0].screen_name);
  console.log('id '+String(i)+ '= '+mens.mentions[0].status_id);
  console.log('name '+String(i)+ '= '+mens.mentions[0].name);
  
  
   }
  } else {
    getDate();
    mention_text=''; // clear mention_text
    document.getElementById("foam").innerHTML+=datetime+': '+mens.message+'<br />';
   console.log('no new mentions');
  }
  
  //speakTest(textu);
  
    }
catch (err){
  console.log('error on loading JSON = '+err);
    }
  });
}

window.periody={{period}}*1000;
window.toggler=1;
function harvest (){
	document.getElementById("framer").src = "http://cloudenstein.rosemarybeetle.org/recent_mentions";
	console.log('inside harvest')
}
var vari; // global variable
function toggle_harvesting (){

	if (window.toggler==1){
		console.log('inside toggle_harvesting() toggler=1')
			vari = setInterval(function(){ mentions()},window.periody);
			//vari = setInterval(function(){ mentions()},window.periody);
			window.toggler=0;
		}
	else if (window.toggler==0)
		{
			clearInterval(vari);
			console.log('inside toggle_harvesting() toggler=0')
			window.toggler=1;
			
		}

} 
