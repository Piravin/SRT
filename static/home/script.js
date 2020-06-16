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
    fetch('show_slide')
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