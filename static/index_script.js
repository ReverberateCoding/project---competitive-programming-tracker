let text1 = document.getElementById('text2');
let url = window.location.href;

url = String(url)

username = url.split("/")
username = username[username.length - 1]

text1.innerHTML = `Username: ${username}`
