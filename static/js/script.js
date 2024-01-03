console.log("Script loaded!");

const updateImage1 = () => {
    var image1 = document.getElementById('dynamicDropdown1').value;

    var imageDisplay1 = document.getElementById('champImage1');

    if (image1 === "") {
        imageDisplay1.style.display = 'none';
        imageDisplay1.src = '';
    }
    else {
        console.log("HERE 11")
        var champImageLocation1 = '/static/champion/' + image1;
        imageDisplay1.src = champImageLocation1;
    }
}

const updateImage2 = () => {
    var image2 = document.getElementById('dynamicDropdown2').value;
    var imageDisplay2 = document.getElementById('champImage2');

    if (image2 === "") {
        imageDisplay2.style.display = 'none';
        imageDisplay2.src = '';
    }
    else {
        console.log("HERE 22")
        var champImageLocation2 = '/static/champion/' + image2;
        imageDisplay2.src = champImageLocation2;
    }
}

const updateImage3 = () => {
    var image3 = document.getElementById('dynamicDropdown3').value;
    var imageDisplay3 = document.getElementById('champImage3');

    if (image3 === "") {
        imageDisplay3.style.display = 'none';
        imageDisplay3.src = '';
    }
    else {
        var champImageLocation3 = '/static/champion/' + image3;
        imageDisplay3.src = champImageLocation3;
    }
}

const updateImage4 = () => {
    var image4 = document.getElementById('dynamicDropdown4').value;
    var imageDisplay4 = document.getElementById('champImage4');

    if (image4 === "") {
        imageDisplay4.style.display = 'none';
        imageDisplay4.src = '';
    }
    else {
        console.log("HERE 4")
        var champImageLocation4 = '/static/champion/' + image4;
        imageDisplay4.src = champImageLocation4;
    }
}

const updateImage5 = () => {
    var image5 = document.getElementById('dynamicDropdown5').value;
    var imageDisplay5 = document.getElementById('champImage5');
    if (image5 === "") {
        imageDisplay5.style.display = 'none';
        imageDisplay5.src = '';
    }
    else {
        console.log("HERE 5")
        var champImageLocation5 = '/static/champion/' + image5;
        imageDisplay5.src = champImageLocation5;
    }
}