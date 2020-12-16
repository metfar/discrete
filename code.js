function hs(nam){
	a=document.getElementById(nam).style.display;
	if(a=="none"){
		document.getElementById(nam).style.display="block";
	 }else{
		document.getElementById(nam).style.display="none";
		}
	return(1);
}

function toggleStyle(nam){
if(nam!="light"){
document.getElementById("thestyle").href="dark.css";
 }else{
document.getElementById("thestyle").href="light.css";
	}
	return(1);
}
