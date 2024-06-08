let text1 = document.getElementById('text1');
let url = window.location.href;

url = String(url)

username = url.split("/")
username = username[username.length - 1]

text1.innerHTML = `Username: ${username}`

document.addEventListener('DOMContentLoaded', () => {
    let category_checkboxes = document.querySelectorAll('.category-checkbox');
    let subcategory_checkboxes = document.querySelectorAll('.subcategory-checkbox')
    category_checkboxes.forEach(category_checkbox => {
        category_checkbox.addEventListener('change', () => {
            //Change checkboxes
            subcategory_checkboxes.forEach(subcategory_checkbox => {
                subcategory_checkbox_id = String(subcategory_checkbox.getAttribute('id'));
                category_checkbox_status = category_checkbox.checked;
                category_checkbox_id = String(category_checkbox.getAttribute('id'));
                if(category_checkbox_id == subcategory_checkbox_id.split('_')[0]){
                    subcategory_checkbox.checked = category_checkbox_status;
                }
            });
        });
    });
    subcategory_checkboxes.forEach(subcategory_checkbox => {
        subcategory_checkbox.addEventListener('change', () => {
            //Check selected
            let t = document.querySelectorAll('.not-selected-cell');
            for(i of t){
                console.log(i.getAttribute('id'));
            }
        });
    });
});
