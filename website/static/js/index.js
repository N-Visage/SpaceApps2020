var filter = document.getElementsByClassName("filter")[0];
var clickIcon = filter.getElementsByClassName("click-icon")[0];

clickIcon.addEventListener("click", openFilter);

function closeFilter() {
    filter.style.marginLeft = "88.5%";
    clickIcon.innerHTML = "Search By Area&nbsp;&nbsp;<span class='material-icons'>filter_list</span>";

    clickIcon.removeEventListener("click", closeFilter);
    clickIcon.addEventListener("click", openFilter);

}

function openFilter() {
    filter.style.marginLeft = "64%";
    clickIcon.innerHTML = "Close Search&nbsp;&nbsp;<span class='material-icons'>clear</span>";

    clickIcon.removeEventListener("click", openFilter);
    clickIcon.addEventListener("click", closeFilter);
}