function showalert(){
    var username=document.getElementById('username').value;
    var first_name=document.getElementById('first_name').value;
    var Last_name=document.getElementById('Last_name').value;
    var Email=document.getElementById('Email').value;
    var PASSWORD=document.getElementById('PASSWORD').value;
    var CONFIRM_PASSWORD=document.getElementById('CONFIRM_PASSWORD').value;

    if(!username || !first_name || !Last_name || !Email || !PASSWORD || !CONFIRM_PASSWORD ){
        alert('Please fill out the required field');
    }
    else{



           alert('Registration Succesfull.Now u can login');
    }
}