function validate(){
    var pattern1=/^[a-zA-Z ]{3,}$/;
    var pattern3= /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    var pattern4=/^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*]).{8,}$/;
    var fname=document.getElementsByName("FirstName");
    var lname=document.getElementsByName("LastName");
    var email=document.getElementsByName("Email");
    var pass=document.getElementsByName("Password");
    var cpass=document.getElementsByName("ConfirmPassword");
    var na=fname[0].value;
    var ln=lname[0].value;
    var em=email[0].value;
    var pa=pass[0].value;
    var cp=cpass[0].value;
    if(na.match(pattern1))
    {
        if(ln.match(pattern1))
        {
            if(em.match(pattern3))
            {
                if(pa.match(pattern4))
                {
                    if(pa==cp)
                    {
                        alert("Registration Succesfull");
                        return true;
                    }
                    else{
                        alert("Password and Confirm Password are not same");
                        return false;
                    }
                }
                else{
                    alert("Password is Weak");
                    return false;
                }
            }
            else{
                alert("Email is invalid");
                return false;
            }
        }
        else{
            alert("Last Name is invalid");
            return false;
        }
    }
    else{
        alert("First Name is invalid");
        return false;
    }
}
