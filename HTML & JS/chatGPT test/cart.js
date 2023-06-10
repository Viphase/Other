let price1 = 0;
let price2 = 0;
let price3 = 0;

let quantity1 = localStorage.getItem("Apple juice");
let quantity2 = localStorage.getItem("Mango");
let quantity3 = localStorage.getItem("Chocolate bar");

let total1;
let total2;
let total3;

let cart1 = localStorage.getItem("cart1");
let cart2 = localStorage.getItem("cart2");
let cart3 = localStorage.getItem("cart3");

let tax = 0.13;
let taxPrice = 0;

let totalp = 0;
let subtotal = 0;

var rounded = function(number){
    return Math.round(parseFloat(number) * 100) / 100;
}

window.onload = function()
{
    if(cart1 == null)
    {
        document.getElementById("p1").innerHTML;
        document.getElementById("price1").innerHTML;
        document.getElementById("quantity1").innerHTML;
        document.getElementById("total1").innerHTML;
    }
    
    else(cart1 == "Apple juice")
    {
        document.getElementById("p1").innerHTML = cart1;
        price1 += 25.99;
        total1 = price1 * quantity1;
        document.getElementById("price1").innerHTML = price1;
        document.getElementById("quantity1").innerHTML = quantity1;
        document.getElementById("total1").innerHTML = total1;
    }
    
    if(cart2 == null)
    {
        document.getElementById("p2").innerHTML;
        document.getElementById("price2").innerHTML;
        document.getElementById("quantity2").innerHTML;
        document.getElementById("total2").innerHTML;
    }
    else(cart2 == "Mango")
    {
        document.getElementById("p2").innerHTML = cart2;
        price2 += 34.99;
        total2 = price2 * quantity2;
        document.getElementById("price2").innerHTML = price2;
        document.getElementById("quantity2").innerHTML = quantity2;
        document.getElementById("total2").innerHTML = total2;
    }
    
    if(cart3 == null)
    {
        document.getElementById("p3").innerHTML;
        document.getElementById("price3").innerHTML;
        document.getElementById("quantity3").innerHTML;
        document.getElementById("total3").innerHTML;
    }
    else(cart3 == "Chocolate bar")
    {
        document.getElementById("p3").innerHTML = cart3;
        price3 += 29.99;
        total3 = price3 * quantity3;
        document.getElementById("price3").innerHTML = price3;
        document.getElementById("quantity3").innerHTML = quantity3;
        document.getElementById("total3").innerHTML = total3;
    }

    taxPrice = rounded((total1 + total2 + total3) * tax);
    document.getElementById("tax").innerHTML = taxPrice;

    subtotal = rounded(total1 + total2 + total3);
    document.getElementById("subtotal").innerHTML = subtotal;

    totalp = rounded(subtotal + taxPrice);
    document.getElementById("totalp").innerHTML = totalp;
}