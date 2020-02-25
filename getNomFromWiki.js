// https://fr.wikipedia.org/wiki/Liste_des_noms_de_famille_les_plus_courants_en_France

cls = document.getElementsByClassName('page_h');
var nameList = new Array();
for (i of cls){
    nameList.push(i.innerText)
}
console.log(nameList);

// https://simple.wikipedia.org/wiki/List_of_cities_in_France

tds = $('.wikitable').find('tr td');
var homeList = new Array();

for (td = 0; td < tds.length; td+=5) {
    homeList.push(tds[td].innerText)
}

console.log(homeList)