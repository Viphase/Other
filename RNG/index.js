let num;

document.getElementById("btn").onclick = function()
{
    console.log("click!");
    num = Math.floor(Math.random() * 100);
    document.getElementById("num").innerHTML = num;
}