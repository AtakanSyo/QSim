// THIS CODE NEEDS TO BE OPTIMIZED!!!!

// Get the root element
var root = document.querySelector(':root');
var rs = getComputedStyle(root);
var backgroundColor = rs.getPropertyValue('--blogBackgroundColor');
var dominantRGB = rs.getPropertyValue('--dominantRGB');

let dominantRGBArr = dominantRGB.slice(
    dominantRGB.indexOf("(") + 1, 
    dominantRGB.indexOf(")")
).split(",");
// Convert to integer
var colorEffectIndex = 10;

for(var i = 0; i < dominantRGBArr.length; i++){
    dominantRGBArr[i] = parseInt(dominantRGBArr[i]/colorEffectIndex);
}

var backgroundColorArr = backgroundColor.slice(
    backgroundColor.indexOf("(") + 1, 
    backgroundColor.indexOf(")")
).split(",");

for(var i = 0; i < backgroundColorArr.length; i++){
    backgroundColorArr[i] = parseInt(backgroundColorArr[i])+dominantRGBArr[i];
}

r = backgroundColorArr[0];
g = backgroundColorArr[1];
b = backgroundColorArr[2];

var newColor = "rgb("+`${r}`+","+`${g}`+","+`${b}`+")";

root.style.setProperty('--blogBackgroundColor', String(newColor));