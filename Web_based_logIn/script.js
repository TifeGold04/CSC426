function login(){

let user =
document.getElementById("username").value;

let pass =
document.getElementById("password").value;

if(user=="" || pass==""){
document.getElementById("message").innerHTML=
"Please fill all fields!";
}

else if(user=="admin" && pass=="1234"){
document.getElementById("message").innerHTML=
"Login Successful!";
}

else{
document.getElementById("message").innerHTML=
"Invalid Username or Password!";
}
}

function resetForm(){
document.getElementById("username").value="";
document.getElementById("password").value="";
document.getElementById("message").innerHTML="";
}