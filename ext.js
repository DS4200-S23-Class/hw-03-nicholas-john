function changecolor(){
	let a = Math.random() * 256;
	let b = Math.random() * 256;
	let c = Math.random() * 256;
	let x = "rgb("+a.toString()+","+b.toString()+","+c.toString()+")";
	document.getElementById('shift').style.color = x;
}
