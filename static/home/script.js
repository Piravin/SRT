var navbar = document.getElementById("navbar");
var navpos = navbar.offsetTop;
window.onscroll = ()=>{
    if(window.pageYOffset > navpos){
        navbar.classList.add("stickynav");
        navbar.classList.remove("navbar");
    }else{
        navbar.classList.remove("stickynav");
        navbar.classList.add("navbar");
    }
};
var pages = document.getElementsByClassName("page");
for(let i=0; i<pages.length; i++){
    pages[i].style.height = navbar.offsetHeight;
}

function initAll(){
    var savebtn = document.getElementById("save_msg");
    savebtn.onclick = saveMsg;
    var slide = document.getElementById("slide");
    var slilink = document.getElementById("slilink");
}

var slide_list,title_list,link_list,dest_list;
title_list=[];
link_list=[];
dest_list=[];
calling();
function calling(){
    fetch('http://localhost:8000/show_slide')
    .then((resp)=>resp.json())
    .then(function(data){
        slide_list=data;
        for(var i in slide_list){
            title_list[i]=slide_list[i].title;
            link_list[i]=slide_list[i].slide;
            dest_list[i]=slide_list[i].slide_link;
        }
    })
}


var slideIndex = 1;
slideShow(slideIndex);

function plusSlides(n){
    slideShow(slideIndex += n);
}

function currentSlide(n){
    slideShow(slideIndex=n);
}
function slideShow(n){
    if(n>link_list.length){slideIndex=1;}
    if(n<1){slideIndex=link_list.length;}
    slide.src=link_list[slideIndex-1];
    slilink.href = dest_list[slideIndex-1];
}
setInterval(()=>{plusSlides(1);},5000);
const parallax = document.getElementById("parallex1");
window.addEventListener("scroll",function(){
    
    var offset = window.pageYOffset;
    parallax.style.backgroundPositionY = offset*0.6 + "px";
})
// var sponcer = document.getElementById("1");
//         var sponcers = document.getElementsByClassName("sponcer");
//         var sponcer_no = sponcers.length;
//         var scrolable = sponcer.offsetWidth * (sponcer_no-1) + 0.5*sponcer.offsetWidth;
//         var p = 0.1;
//         var v=p;
//         var timer = setInterval(()=>{
//             if (p<scrolable){
//                 sponcer.style.marginLeft = "-"+p+"px";
//                 p+=1;
//                 v=p;
//             }
//             else{
//                 sponcer.style.marginLeft = "-"+v+"px";
//                 v-=1;
//                 if(v<=0){
//                     p=0;
//                 }
//             }
//         },10);



function saveMsg(){
    var req = new XMLHttpRequest();
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var mobile = document.getElementById("mobile").value;
    var subject = document.getElementById("subject").value;
    var msg = document.getElementById("msg").value;
    req.setRequestHeader("Content-type", "application/json");
    var url = 'sv_msg';
    req.onreadystatechange = function(){
        if(this.readyState==4 && this.status==200){
            alert(req.responseText);
        }
    };
    var data = JSON.stringify({'name':'name','email':'email','mobile':'mobile','subject':'subject','message':'msg'});
    req.open("POST",url,true);
    req.send(data);
}