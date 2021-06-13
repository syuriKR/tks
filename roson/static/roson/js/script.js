var categories = [
    'osozai',
    'osozai_salad', 
    'bento',
    "childbento",
    "desert",
    "fly",
    "child",
    "gratin",
    "instant",
    "konamono",
    "noodle",
    "onigiri",
    "pasta",
    "salad",
    "soup"
]

function change_categorie(id){
    for (let i = 0; i < categories.length; i++){
        var div = document.querySelectorAll("." + categories[i]);
            div.forEach(function(elem){
            elem.style.display = "none";
        });

    }
    var display = document.getElementById(id);
    var div = document.querySelectorAll("." + id);
            div.forEach(function(elem){
            elem.style.display = "";
        });
};
function display_all(){
    for (let i = 0; i < categories.length; i++){
        var div = document.querySelectorAll("." + categories[i]);
            div.forEach(function(elem){
            elem.style.display = "";
        });
    }
}
