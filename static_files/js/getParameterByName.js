function getParameterByName(name)
{
    name = name.replace(/[\[]/, "\\\[").replace(/[\]]/, "\\\]");
    var regexS = "[\\?&]" + name + "=(.*?)(#|&|$)";
    var regex = new RegExp(regexS);
    var results = regex.exec(window.location.search);
    if(results == null)
    {
        return "";
    }
    else
    {
        return decodeURIComponent(results[1].replace(/\+/g, " "));
    }
}

function fill_data()
{
    var span_surname_name = document.getElementById('surname_name');
    var span_name = document.getElementById('name');
    var span_age = document.getElementById('age');
    var span_surname = document.getElementById('surname');
    var span_otchestvo = document.getElementById('otchestvo');
    var span_adress = document.getElementById('adress');
    var a_adress = document.getElementById('adress_link');
    var span_skype = document.getElementById('skype');
    var a_skype = document.getElementById('skype_link');
    var span_email = document.getElementById('email');
    var a_email = document.getElementById('email_link');
    var span_raite = document.getElementById('raite');
    var rait = document.getElementById('rait');
    var image = document.getElementById('image');
    var number = getParameterByName('number'); //Get number of student
    span_surname_name.innerHTML = data[number].surname_name;
    span_name.innerHTML = data[number].name;
    span_age.innerHTML = data[number].age;
    span_surname.innerHTML = data[number].surname;
    span_otchestvo.innerHTML = data[number].otchestvo;
    span_adress.innerHTML = data[number].adress;
    span_skype.innerHTML = data[number].skype;
    span_email.innerHTML = data[number].email;
    span_raite.innerHTML = (data[number].raite/8).toFixed();
    image.src = data[number].image;
    a_skype.href = 'skype:'+(data[number].skype).toString();
    a_email.href = 'mailto:'+(data[number].email).toString();
    a_adress.href = 'https://www.google.com.ua/maps/place/'+(data[number].adress).toString();
    rait.style.width = (data[number].raite/8).toString()+"%";
    if (data[number].raite/8 > 90) {
        rait.classList.add("progress-bar-success");
    }
    else if (data[number].raite/8 > 80) {
        rait.classList.add("progress-bar-warning");
    }
    else {
        rait.classList.add("progress-bar-danger");
    }
    var num_r_list = [];
    for (var i = data.length - 1; i >= 0; i--) {
        num_r_list[i] = data[i].raite
    };
    num_r_list.sort().reverse();
    for (var i = num_r_list.length - 1; i >= 0; i--) {
        if (data[number].raite == num_r_list[i]) {
            num_r = i + 1;
        }
    var span_num_r = document.getElementById('num_r');
    span_num_r.innerHTML = num_r;
    };
    var img_list = ["img_1","img_2","img_3","img_4","img_5","img_6","img_7","img_8"];
    for (var i = data[number].kr.length - 1; i >= 0; i--) {
        var img = document.getElementById(img_list[i]);
        if (data[number]["kr"][i] == false) {
            img.src = "http://www.environskimberley.org.au/wp-content/uploads/2011/03/make-yourself-heard1.jpg1-171x180.jpg";
        }
        else {

            img.src = "http://www.oxcheer.com/images/f0982c4ab87148dd941765cab0bcab1f_171x180.png";
        }
    };
}