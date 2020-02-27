article = document.getElementById("atl");

function indexClick() {
    location.reload();
}
function getValuableStudent() {

}

function studentClick() {
    article.innerHTML = '<p>The most valuable student is </p>'+'<table>\n' +
        '  <tr>\n' +
        '    <th>Dropout Students Campus ID</th>\n' +
        '    <th>Reason</th>\n' +
        '  </tr>\n' +
        '  <tr>\n' +
        '    <td>Alfreds Futterkiste</td>\n' +
        '    <td>Maria Anders</td>\n' +
        '  </tr>\n' +
        '  <tr>\n' +
        '    <td>Centro comercial Moctezuma</td>\n' +
        '    <td>Francisco Chang</td>\n' +
        '  </tr>\n' +
        '  <tr>\n' +
        '    <td>Ernst Handel</td>\n' +
        '    <td>Roland Mendel</td>\n' +
        '  </tr>\n' +
        '  <tr>\n' +
        '    <td>Island Trading</td>\n' +
        '    <td>Helen Bennett</td>\n' +
        '  </tr>\n' +
        '  <tr>\n' +
        '    <td>Laughing Bacchus Winecellars</td>\n' +
        '    <td>Yoshi Tannamuri</td>\n' +
        '  </tr>\n' +
        '  <tr>\n' +
        '    <td>Magazzini Alimentari Riuniti</td>\n' +
        '    <td>Giovanni Rovelli</td>\n' +
        '  </tr>\n' +
        '</table>'+
        '<div  style="margin-top :20px"><b>The reason why there are more students in one region and few in another:</b>'+
        '<strong style="color:black;"><br>Economic and transportation gap</strong></div>';
}

function schoolClick() {
    article.innerHTML =
        '<div><b>How to revitalize campuses:</b>'+
        '<Strong style="color:black;"><br>According to big data statistics, students\' attendance rate is relatively low.SUPINFO should strengthen the management of students and ensure the quality of teaching.</Strong></div>'+
        '<div style="margin-top: 20px"><b>Who are SUPINFO\'s competitors who are poaching our students</b>'+
        '<Strong style="color:black;"><br>没有对手</Strong>'+
        '<table><tr><th>School</th></tr>'+
        '<tr><td>ESCE</td></tr></table></div>'+
        '<div style="margin-top: 20px"><b>How to attract more students:</b>'+
        '<Strong style="color:black;"><br>According to big data statistics, SUPINFO should strengthen publicity on schools in the campus with few students</Strong></div>'+
        '';
}

function internClick() {
    article.innerText = '没有学生找到工作，建议封校';
    article.innerHTML =
    '<div><b>The average length of time graduates are hired:</b>'+
    '<Strong style="color:black;"><br>10 年</Strong></div>'+
    '<div style="margin-top: 20px"><b>Which companies recruit the most students from supinfo:</b>'+
    '<Strong style="color:black;"><br>Google</Strong></div>'+
    '<div style="margin-top: 20px"><b>Which regions have more Pro contracts and why:</b>'+
    '<Strong style="color:black;"><br>Paris</Strong></div>'+
    '<Strong style="color:black;">According to big data statistics, the number of internships in Paris is the largest, and there are more employment opportunities in Paris.</Strong>';
}