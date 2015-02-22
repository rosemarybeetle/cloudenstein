eye_toggle=0;
function blink2(target){
	console.log('blink2 presssed');
  try {
  	var eye=document.getElementById(target);
  	if (eye_toggle==0){
  		eye_toggle=1;
  	 	eye.style.opacity=0;
  } else 
  {
  	eye_toggle=0;
  	eye.style.opacity=1;
  }
   }
catch (err){
  console.log('error 1 = '+err)
    }
  }
//==========================
function cycle_n (target,n,full){
  console.log('insidecycle_n');
  console.log('arguments = target: '+target+', n: '+String(n)+', full: '+full);
	// n is the number of keyframe components that comprise this animation, full = flag for type of cycle
	// this function will start with 0 and cycle to n and if full=true will return to 0, if false will stop at n
for (x=0; x<=n;x++) {
console.log('inside for loop. x= '+String(x));
var tgt=target+String(x);
console.log('tgt = '+String(tgt));
var obj=document.getElementById(tgt);
obj.style.opacity=0.2;
  }

} // end of cycle_n
//==========================

//==========================  backup  ======================================
//var vari;
var random_checker=0;
window.fade_t=5; // rate of fade decay in milliseconds
window.fade_f=.2; // amount of fade
window.fade_inc=10; // increments of fade

function eye_open(){
  // next 6 lines needed to put pupils in right place if window gets resized
  var ww = window.innerWidth;
  console.log('ww = window.innerWidth = '+ww)
  lll=String((ww*.25)+'px')
  rrr=String((ww*.65)+'px')
  document.getElementById('pupil_left').style.left=lll;
  document.getElementById('pupil_right').style.left=rrr;
  document.getElementById('eye_left_0').style.opacity=1;
  for (x=1;x<=3;x++)
    {
      obj='eye_left_'+String(x);
  document.getElementById(obj).style.opacity=0;
}
document.getElementById('eye_right_0').style.opacity=1;
  for (x=1;x<=3;x++)
    {
      obj='eye_right_'+String(x);
  document.getElementById(obj).style.opacity=0;
}
window.eeel = document.getElementById('pupil_left').offsetLeft;
window.eeer = document.getElementById('pupil_right').offsetLeft;
console.log('eee LEFT = '+eeel+'eeeRIGHT = '+eeer);
eye_blink_both();
eye_blink_both();
} // =============================================

$( window ).resize(function() {
  // var sy = document.getElementById('eye_slider');//.value=50;
  // sy.value=50;
  // console.log('slidey = '+ sy);
  eye_open();
  console.log('resizing');
});

// ===============================================
function eye_blink_left (){
  coont=0;
  console.log('inside eyeblink()');
    document.getElementById('eye_left_1').style.opacity=1;
for (x=0;x<window.fade_inc;x++) {

delay=(1+x)*window.fade_t;
fade0 =window.setTimeout(function(){document.getElementById('eye_left_0').style.opacity-=window.fade_f;},delay);
coont++;
console.log('delay0= '+delay)
}

document.getElementById('eye_left_2').style.opacity=1;
for (x=0;x<window.fade_inc;x++) {
delay=(1+x)*window.fade_t;
fade1 =window.setTimeout(function(){document.getElementById('eye_left_1').style.opacity-=window.fade_f;},delay);
coont++;
console.log('delay1= '+delay)
}
document.getElementById('eye_left_3').style.opacity=1;
for (x=0;x<window.fade_t;x++) {

delay=(1+x)*window.fade_t;
fade2 =window.setTimeout(function(){document.getElementById('eye_left_2').style.opacity-=window.fade_f;},delay);
coont++;
console.log('delay2= '+delay)

}

delay=((coont-1)*window.fade_t);
console.log('delayfinal= '+delay)
//window.setTimeout(function(){document.getElementById('eye_left_0').style.opacity=1},delay);
window.setTimeout(function(){document.getElementById('eye_left_0').style.opacity=1;document.getElementById('eye_left_3').style.opacity=0;},delay);

} // end of blink left
//====================================================================

function eye_blink_right (){
  coont=0;
  console.log('inside eyeblink()');
    document.getElementById('eye_right_1').style.opacity=1;
for (x=0;x<window.fade_inc;x++) {

delay=(1+x)*window.fade_t;
fade0r =window.setTimeout(function(){document.getElementById('eye_right_0').style.opacity-=window.fade_f;},delay);
coont++;
console.log('delay0= '+delay)
}

document.getElementById('eye_right_2').style.opacity=1;
for (x=0;x<window.fade_inc;x++) {
delay=(1+x)*window.fade_t;
fade1r =window.setTimeout(function(){document.getElementById('eye_right_1').style.opacity-=window.fade_f;},delay);
coont++;
console.log('delay1= '+delay)
}
document.getElementById('eye_right_3').style.opacity=1;
for (x=0;x<window.fade_t;x++) {

delay=(1+x)*window.fade_t;
fade2r =window.setTimeout(function(){document.getElementById('eye_right_2').style.opacity-=window.fade_f;},delay);
coont++;
console.log('delay2= '+delay)

}

delay=((coont-1)*window.fade_t);
console.log('delayfinal= '+delay)
//window.setTimeout(function(){document.getElementById('eye_right_0').style.opacity=1},delay);
window.setTimeout(function(){document.getElementById('eye_right_0').style.opacity=1;document.getElementById('eye_right_3').style.opacity=0;},delay);

} // =================end blink right 

// =========== eye controlling input slider ===================
function mirror() {
  var ss = document.getElementById('eye_slider').value;
  document.getElementById('output').innerHTML=ss;
}

function move_eyes() {
  var gg = document.getElementById('eye_slider').value;
if (gg <110) {
  
  //var eell = document.getElementById('pupil_left').offsetLeft;
  //console.log ('eell = '+eell);
  ggg=String((window.eeel)-(50-gg)+'px')
  hhh=String((window.eeer)-(50-gg)+'px')
  document.getElementById('pupil_left').style.left=ggg;
  document.getElementById('pupil_right').style.left=hhh;
  console.log ('ggg = '+ggg);
 }
} //=============================================


// ==============================================


function eye_blink_both () {
eye_blink_left ();
eye_blink_right ();
}
//==========================  backup  ======================================

function toggle_harvesting (){

  if (window.toggler==1){
    console.log('inside toggle_harvesting() toggler=1')
      vari = setInterval(function(){ mentions()},window.periody);
      document.getElementById("heado").innerHTML='Mentionising...';
      getDate();
      document.getElementById("foam").innerHTML+=datetime+': Logs started...<br />';


      //vari = setInterval(function(){ mentions()},window.periody);
      window.toggler=0;
    }
  else if (window.toggler==0)
    {
      clearInterval(vari);
      console.log('inside toggle_harvesting() toggler=0')
      document.getElementById("heado").innerHTML='Mentionising paused<br />';
      getDate();
      document.getElementById("foam").innerHTML+=datetime+': Logs paused...';


      window.toggler=1;
      
    }

} 