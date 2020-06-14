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

var slideIndex = 1;
slideShow(slideIndex);

function plusSlides(n){
    slideShow(slideIndex += n);
}

function currentSlide(n){
    slideShow(slideIndex=n);
}
function slideShow(n){
    let i;
    var slides = document.getElementsByClassName("slide");
    var dots = document.getElementsByClassName("dot");
    slilent=slides.length;
    if(n>slides.length){slideIndex=1;}
    if(n<1){slideIndex=slides.length;}
    for(i=0;i<slides.length;i++){
        slides[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[slideIndex-1].style.display = "block";
    dots[slideIndex-1].className += " active";
}
setInterval(()=>{plusSlides(1);},5000);
const parallax = document.getElementById("parallex1");
window.addEventListener("scroll",function(){
    
    var offset = window.pageYOffset;
    parallax.style.backgroundPositionY = offset*0.6 + "px";
})
var sponcer = document.getElementById("1");
        var sponcers = document.getElementsByClassName("sponcer");
        var sponcer_no = sponcers.length;
        var scrolable = sponcer.offsetWidth * (sponcer_no-1) + 0.5*sponcer.offsetWidth;
        var p = 0.1;
        var v=p;
        var timer = setInterval(()=>{
            if (p<scrolable){
                sponcer.style.marginLeft = "-"+p+"px";
                p+=1;
                v=p;
            }
            else{
                sponcer.style.marginLeft = "-"+v+"px";
                v-=1;
                if(v<=0){
                    p=0;
                }
            }
        },10);


function initAll(){
    var savebtn = document.getElementById("save_msg");
    savebtn.onclick = saveMsg;
}


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