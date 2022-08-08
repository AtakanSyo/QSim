const DarkModeButton = document.getElementById("Dark-Mode-Button");
const PantheonButton = document.getElementById("Pantheon-Button");
const htmlTag = document.getElementsByTagName("html")[0];
const writings = document.querySelectorAll('p,h2');
const pageWrapper = document.getElementsByClassName("page-wrapper")[0];
const symbols = document.getElementsByClassName("Symbol");
const visuals = document.getElementsByClassName("visual");
const quotations = document.getElementsByClassName("quotation");
var toggle = 0;

function DarkModeToggle() { // Put some CSS modifications in here.
  if (toggle==0){
  	root.style.setProperty('--blogBackgroundColor',  "#161616");
  	if (typeof pageWrapper !== 'undefined') {
	  	pageWrapper.style.backgroundBlendMode = "darken";	
  	}
	  for (const writing of writings) {
	  writing.classList.add("dark-mode-invert");
	 }
	  for (const symbol of symbols) {
	  symbol.classList.add("dark-mode-invert");
	 }
	  for (const visual of visuals) {
	  visual.classList.add("dark-mode-visual");
	 }
	  for (const quotation of quotations) {
	  quotation.classList.add("dark-mode-quotation");
	 }
  	toggle = 1;
  }
  else{ // Light Mode
  	root.style.setProperty('--blogBackgroundColor', String(newColor));
  	if (typeof pageWrapper !== 'undefined') {
	  	pageWrapper.style.backgroundBlendMode = "lighten";
  	}
  	htmlTag.style.transitionDuration = "0.5s";
	  for (const writing of writings) {
	  writing.classList.remove("dark-mode-invert");
	 }
	  for (const symbol of symbols) {
	  symbol.classList.remove("dark-mode-invert");
	 }
	  for (const visual of visuals) {
	  visual.classList.remove("dark-mode-visual");
	 }
	  for (const quotation of quotations) {
	  quotation.classList.remove("dark-mode-quotation");
	 }
  	toggle = 0;
  }
}

DarkModeButton.onclick = DarkModeToggle;