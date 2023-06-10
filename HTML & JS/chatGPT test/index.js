let quantity1 = 0;
let quantity2 = 0;
let quantity3 = 0;

document.getElementById("b1").onclick = function()
{
    quantity1 += 1;
    localStorage.setItem("cart1", "Apple juice");
    localStorage.setItem("Apple juice", quantity1);
}

document.getElementById("b2").onclick = function()
{
    quantity2 += 1;
    localStorage.setItem("cart2", "Mango");
    localStorage.setItem("Mango", quantity2);
}

document.getElementById("b3").onclick = function()
{
    quantity3 += 1;
    localStorage.setItem("cart3", "Chocolate bar");
    localStorage.setItem("Chocolate bar", quantity3);
}
