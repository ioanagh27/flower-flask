function toggleColour(event) {
    if (event.currentTarget.style.backgroundColor == event.currentTarget.style.borderColor) {
        event.currentTarget.style.backgroundColor = "#333333";
    } else {
        event.currentTarget.style.backgroundColor = event.currentTarget.style.borderColor;
    }
}    

document.querySelectorAll(".flower").forEach(f => {
    f.addEventListener("click", toggleColour);
})
