var random_checker=0;
window.fade_t=5; // rate of fade decay in milliseconds
window.fade_f=.2; // amount of fade
window.fade_inc=10; // increments of fade

eye_toggle=0;
window.fade_blush_t_d= 60; // rate of fade decay in milliseconds
window.fade_blush_f_d=.2; // amount of fade
window.fade_blush_inc_d=20; // increments of fade
// blush fade parameters
window.blush_base=0.21;
window.blusher_factor= 1; /// starting blusher
window.blusher_denom=30;
window.fade_blush_t= 155; // rate of fade decay in milliseconds
window.fade_blush_f=.03; // amount of fade
window.fade_blush_inc=30; // increments of fade
// end f blushing
// frown parameters
window.frown_toggle=0; //default is no frowning
window.frown_factor=0; // initialise frown increment
window.frown_denom=4;
window.frown_fade_t= 45; // rate of frown fade decay in milliseconds
window.frown_blush_inc=6; // increments of frown

// end frown
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





// ====================== noses ======================
function nose_init() {document.getElementById('nose_0').style.opacity=1;
  for (x=1;x<=3;x++)
    {
      obj='nose_'+String(x);
  document.getElementById(obj).style.opacity=0;
}
document.getElementById('nose_frown').style.opacity=0; // frown lines
}
// ===================== end noses ===================


// ========================================================================================
// ===================== START WRINKLES ======================
// ========================================================================================
function nose_wrinkle() {
  console.log('');
  console.log('Inside nose_wrinkle ()...');
  console.log('');
  wrink_inc=3; // n where n=number of nose states in wrinkle
  wrink_t=70; // standard delay period


delay_w=window.wrink_t;
wrink0=window.setTimeout(function(){nose_wrinks(0);},delay_w);
delay_w=2*window.wrink_t;
wrink1=window.setTimeout(function(){nose_wrinks(1);},delay_w);
delay_w=3*window.wrink_t;
wrink2=window.setTimeout(function(){nose_wrinks(2);},delay_w);
delay_w=4*window.wrink_t;
wrink3=window.setTimeout(function(){nose_wrinks(3);},delay_w);

}

function nose_wrinks(wrk){
  console.log('');
  console.log('Inside nose_wrinks('+wrk+')...');
  console.log('');
  var wrk_fade
  if (wrk ==0){
    wrk_fade=3;
  } else {
    wrk_fade=wrk-1;
  }
  gg='nose_'+String(wrk); //generate current nose state name based on wrk argument passed to nose_wrinks
  gg_fade='nose_'+String(wrk_fade);
  console.log("Processing nose_wrinks()"+gg+' inside nose_wrinks()');
  document.getElementById(gg).style.opacity=.4;
  for (x=0;x<wrk;x++)
    {
      if (x!=wrk) {
        if (x=wrk_fade){
          obj='nose_'+String(x);
  document.getElementById(obj).style.opacity=.2;
        } else {
        obj='nose_'+String(x);
  document.getElementById(obj).style.opacity=0;
        }
      } 
  } 
  if (wrk==3){
    nose_wrinkle_2 ();
  }
  nose_opacity_test();
}
// ----------------- the 2 functions above start it ------------
// --------------- the two below retrun it to normal -----------
function nose_wrinkle_2 ()   {
  console.log('');
  console.log('Inside nose_wrinkle_2 ()...');
  console.log('');
wrink_inc=3; // n where n=number of nose states in wrinkle
  wrink_t=80; // standard delay period

  delay_w=window.wrink_t;
wrink0=window.setTimeout(function(){nose_wrinks_return(3);},delay_w);
delay_w=2*window.wrink_t;
wrink1=window.setTimeout(function(){nose_wrinks_return(2);},delay_w);
delay_w=3*window.wrink_t;
wrink2=window.setTimeout(function(){nose_wrinks_return(1);},delay_w);
delay_w=4*window.wrink_t;
wrink3=window.setTimeout(function(){nose_wrinks_return(0);},delay_w);
delay_w=4*window.wrink_t;
wrink4=window.setTimeout(function(){nose_init();},delay_w);
}

function nose_wrinks_return (wrk){
  console.log('');
  console.log('Inside nose_wrinks('+wrk+')...');
  console.log('');
  var wrk_fade
  if (wrk ==0){
    wrk_fade=3;
  } else {
    wrk_fade=wrk-1;
  }
  gg2='nose_'+String(wrk); //generate current nose state name based on wrk argument passed to nose_wrinks
  console.log("Processing nose_wrinks()"+gg+' inside nose_wrinks()');
  document.getElementById(gg2).style.opacity=.6;
  for (x=0;x<wrk;x++)
    { obj2='nose_'+String(x);
      if (x!=wrk) {
        if (x=wrk_fade){
  document.getElementById(obj2).style.opacity=.2;
        } else {
        document.getElementById(obj2).style.opacity=0;
      }
      } 
  }  
  
  if (wrk==0){
    console.log('stop');
  }
  nose_opacity_test(); // this is a test script function
}

function nose_opacity_test(){
  console.log("finally, let's test what is visible");
  for (x=0;x<=3;x++)
    {
  obj='nose_'+String(x);
  console.log('opacity of '+obj+' = '+ document.getElementById(obj).style.opacity);
    }
    console.log('end test');
}

// ========================================================================================
// ===================== START WRINKLES ======================
// ========================================================================================

$( window ).resize(function() {
  // var sy = document.getElementById('eye_slider');//.value=50;
  // sy.value=50;
  // console.log('slidey = '+ sy);
  refresh_face();
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

// ======================== frown =============================
// ============================================================

//
function frown_shade(){
  
  window.frown_factor++;
  var opj=window.frown_factor/window.frown_denom;
  document.getElementById('nose_frown').style.opacity=opj;
  console.log('nose_frown opacity (opj) = '+opj);
  if (opj==1){
  console.log("bingo");
   }

}


function frown_shader (){
  var opj=53*(window.frown_factor/window.frown_denom);
  document.getElementById('nose_frown').style.opacity=opj;
for (x=0;x<window.frown_blush_inc;x++) {
delay_b=(1+x)*window.fade_blush_t;
window.frown_shade_dwn =window.setTimeout(function(){if ((window.frown_factor/window.frown_denom)<1){frown_shade();}},delay_b);
console.log('frown_shade opacity = '+document.getElementById('nose_frown').style.opacity);
console.log('frown delay1= '+delay_b);
  }
}

function frown_unshader (){
  clearTimeout(window.frown_shade_dwn);
  window.frown_factor=0; // initialise frown increment
document.getElementById('nose_frown').style.opacity=0;
}

//
function frown_toggler () {
  if (window.frown_toggle==0) {// toggles depending if they are down aleady
  x=1;
  frown(x); 
  } 
  else if (window.frown_toggle==1){
  x=0;
  frown(x); 
  }
}
function frown (up_dwn){
  
  if (up_dwn==1){
    // blush();
    frown_shader();
  coont=0;
  console.log('inside frown()');
  document.getElementById('eyebrow_left_1').style.opacity=1;
  document.getElementById('eyebrow_right_1').style.opacity=1;
for (x=0;x<window.fade_inc;x++) {

delay=(1+x)*window.frown_fade_t;
fade0 =window.setTimeout(function(){document.getElementById('eyebrow_left_0').style.opacity-=window.fade_f;document.getElementById('eyebrow_right_0').style.opacity-=window.fade_f;},delay);
coont++;
console.log('delay0= '+delay)
}

document.getElementById('eyebrow_left_2').style.opacity=1;
  document.getElementById('eyebrow_right_2').style.opacity=1;
for (x=0;x<window.fade_inc;x++) {
delay=(1+x)*window.fade_t;
fade1 ==window.setTimeout(function(){document.getElementById('eyebrow_left_1').style.opacity-=window.fade_f;document.getElementById('eyebrow_right_1').style.opacity-=window.fade_f;},delay);
coont++;
console.log('delay1= '+delay)
    } // end for 
window.frown_toggle=1;
  } // end if toggle 
  else if (up_dwn==0){
  //   window.blusher_factor= 1; /// starting blusher

  //   document.getElementById('cheek_left').style.opacity=window.blush_base;
  // document.getElementById('cheek_right').style.opacity=window.blush_base;
    
      frown_unshader();
    
    delay=(window.fade_t);
console.log('delayfinal= '+delay)
window.setTimeout(function(){document.getElementById('eyebrow_left_0').style.opacity=1;document.getElementById('eyebrow_right_0').style.opacity=1;document.getElementById('eyebrow_left_2').style.opacity=0;document.getElementById('eyebrow_right_2').style.opacity=0;},delay);
window.frown_toggle=0;
  }
}
//========================== end frown ================================
//=====================================================================

// ========================== blush ===================================
function setblush_opac(){
  
  window.blusher_factor++;
  var opj=window.blusher_factor/window.blusher_denom;
  document.getElementById('cheek_left').style.opacity=opj;
  document.getElementById('cheek_right').style.opacity=opj;
  console.log('cheek_left opacity (opj) = '+opj);
  if (opj==1){
  console.log("bingo");
  blush_down();
  }

}


function blush (){
// document.getElementById('cheek_left').style.opacity=1;
// document.getElementById('cheek_right').style.opacity=1;
for (x=0;x<window.fade_blush_inc;x++) {
delay_b=(1+x)*window.fade_blush_t;
blusher_up =window.setTimeout(function(){if ((window.blusher_factor/window.blusher_denom)<1){setblush_opac();}},delay_b);
console.log('cheek_left opacity = '+document.getElementById('cheek_left').style.opacity);
console.log('blush delay1= '+delay_b);
  }
}



function setblush_opac_2(){ 
  window.blusher_factor--;
  console.log('window.blusher_factor = '+window.blusher_factor);
  var opj_d=window.blusher_factor/window.blusher_denom;
  document.getElementById('cheek_left').style.opacity=opj_d;
  document.getElementById('cheek_right').style.opacity=opj_d;
  console.log('cheek_left opacity (opj_d) = '+opj_d);  
}

function blush_down (){
window.clearTimeout(blusher_up);
console.log('tringo');
console.log('window.blusher_factor/window.blusher_denom = '+window.blusher_factor/window.blusher_denom);
// document.getElementById('cheek_left').style.opacity=1;
// document.getElementById('cheek_right').style.opacity=1;
for (y=0;y<window.fade_blush_inc_d;y++) {
delay_bd=(1+y)*window.fade_blush_t_d;
blusher_down =window.setTimeout(function(){if ((window.blusher_factor)>window.blush_base){setblush_opac_2();}},delay_bd);
console.log('cheek_left opacity down = '+document.getElementById('cheek_left').style.opacity);
console.log('blush delay down= '+delay_bd);
  }
}

// ========================= end blush ========================

// =========== eye controlling input slider ===================
function mirror() {
  var ss = document.getElementById('eye_slider').value;
  document.getElementById('output').innerHTML=ss;
}

function move_eyes() {
  var gag = document.getElementById('eye_slider').value;
   var xx = window.innerWidth;
   console.log('for screen width = '+xx+' , pupil.left = '+window.llll+' , pupil.right = '+window.rrrr)
   adj=((gag-50)/100)*window.eyeball_rf; // this is teh adjustment factor based on slide of range 0 - 50
   
  //  var llll = document.getElementById('pupil_left').style.left;
  // var rrrr = document.getElementById('pupil_right').style.left;
  //ggg=String(((parseFloat(window.llll))-((eb_w/2)-gg))+'px')
  //hhh=String(((parseFloat(window.rrrr))-((eb_w/2)-gg))+'px')
  ggg = String (((parseFloat(window.llll)+adj))+'px');
  hhh = String (((parseFloat(window.rrrr)+adj))+'px');
  document.getElementById('pupil_left').style.left=ggg;
  document.getElementById('pupil_right').style.left=hhh;
  console.log('slider value = '+gag+' , setting pupil.left to: '+ggg+' , and pupil right to be: '+hhh);
 
} //=============================================


function move_eyes_up() {
  var gag_up = document.getElementById('eye_slider_up').value;
   var yy = window.innerWidth;
   console.log('for screen width = '+yy+' , pupil.left = '+window.llll_up+' , pupil.right = '+window.rrrr_up)
   adj_up=((gag_up-50)/100)*window.eyeball_rf_up; // this is teh adjustment factor based on slide of range 0 - 50
   
  //  var llll = document.getElementById('pupil_left').style.left;
  // var rrrr = document.getElementById('pupil_right').style.left;
  //ggg=String(((parseFloat(window.llll))-((eb_w/2)-gg))+'px')
  //hhh=String(((parseFloat(window.rrrr))-((eb_w/2)-gg))+'px')
  ggg_up = String (((parseFloat(window.llll_up)-adj_up))+'px');
  hhh_up = String (((parseFloat(window.rrrr_up)-adj_up))+'px');
  document.getElementById('pupil_left').style.top=ggg_up;
  document.getElementById('pupil_right').style.top=hhh_up;
  console.log('slider value _up = '+gag_up+' , setting pupil.left vertical to: '+ggg_up+' , and pupil right vertical to be: '+hhh_up);
 
} 

//  ===================================================

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


function refresh_face(){
  document.getElementById('cheek_left').style.opacity=window.blush_base;
  document.getElementById('cheek_right').style.opacity=window.blush_base;
  // next 6 lines needed to put pupils in right place if window gets resized
  var ww = window.innerWidth;
  window.eyeball_rf=.07*ww; // radius of eyeball scaled to sceen width (horizontal play)
  window.eyeball_rf_up=.04*ww; // vertical play for eyeball
  if (ww>=980){
    
  console.log('window size is greater than 980 - ww = window.innerWidth = '+ww)
  lll=String((ww*.12)+'px')
  window.llll = lll;
  rrr=String((ww*.33)+'px')
  window.rrrr=rrr;
  document.getElementById('pupil_left').style.left=lll;
  document.getElementById('pupil_right').style.left=rrr;
  lll_up=String((ww*.01));
 rrr_up=String((ww*.01));
  window.llll_up=lll_up;
  window.rrrr_up=rrr_up;
  document.getElementById('pupil_left').style.top=lll_up;
  document.getElementById('pupil_right').style.top=rrr_up;
  document.getElementById('cheek_left').style.opacity=window.blush_base;
  document.getElementById('cheek_right').style.opacity=window.blush_base;
  chk_top=String((ww*.085)+'px')
  document.getElementById('cheek_left').style.top=chk_top;
  document.getElementById('cheek_right').style.top=chk_top;
  

  // cheeks next >>>>>>>>>>>>
  
} else if (ww<980) {
  console.log('window size is less than 980 - ww = window.innerWidth = '+ww);
  lll=String((ww*.22)+'px');
  window.llll = lll;
  rrr=String((ww*.60)+'px');
  window.rrrr=rrr;
  document.getElementById('pupil_left').style.left=lll;
  document.getElementById('pupil_right').style.left=rrr;
lll_up=String((ww*.05));
 rrr_up=String((ww*.05));
  window.llll_up=lll_up;
  window.rrrr_up=rrr_up;
  document.getElementById('pupil_left').style.top=lll_up;
  document.getElementById('pupil_right').style.top=rrr_up;
  //  >>>>>>>>>>>>>>>> cheeks >>>>>>>>>>>>>>>>>>>>>>  //
document.getElementById('cheek_left').style.opacity=window.blush_base;
  document.getElementById('cheek_right').style.opacity=window.blush_base;
  chk_top=String((ww*.14)+'px')
  document.getElementById('cheek_left').style.top=chk_top;
  document.getElementById('cheek_right').style.top=chk_top;
//  <<<<<<<<<<<<<<<< cheeks <<<<<<<<<<<<<<<<<<<<<<<<  //
  
}
nose_init();
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
document.getElementById('eyebrow_left_0').style.opacity=1;
document.getElementById('eyebrow_right_0').style.opacity=1;

  for (x=1;x<=2;x++)
    {
      objl='eyebrow_right_'+String(x);
  document.getElementById(objl).style.opacity=0;
  objr='eyebrow_left_'+String(x);
  document.getElementById(objr).style.opacity=0;
}

window.eeel_up = document.getElementById('pupil_left').offsetTop;
window.eeer_up = document.getElementById('pupil_right').offsetTop;
console.log('window.llll_up = '+ String(window.llll_up)+' , and window.rrrr_up = '+String(window.rrrr_up));
window.eeel = document.getElementById('pupil_left').offsetLeft;
window.eeer = document.getElementById('pupil_right').offsetLeft;


console.log('eee LEFT = '+eeel+'eeeRIGHT = '+eeer);
eye_blink_both();
eye_blink_both();
eye_blink_both();
} // ============================================= end refresh face ======================