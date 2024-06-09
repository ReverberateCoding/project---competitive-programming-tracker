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
                    // Dispatch change event
                    let event = new Event('change');
                    subcategory_checkbox.dispatchEvent(event);
                }
            });
        });
    });
    subcategory_checkboxes.forEach(subcategory_checkbox => {
        subcategory_checkbox.addEventListener('change', () => {
            console.log("What");
            //Initialise path
            let json_path_name = `${window.location.protocol}//${window.location.host}/static/atcoder_tags.json`;
            console.log(json_path_name);
            //Fetch json
            fetch(json_path_name)
                .then(res => res.json()) // the .json() method parses the JSON response into a JS object literal
                .then(atcoder_categories => {

                    let subcategory_checkbox_id = subcategory_checkbox.getAttribute('id');

                    // To iterate over the main categories (e.g., "Dynamic-Programming", "Graph")
                    Object.keys(atcoder_categories).forEach(mainCategory => {

                        console.log("Main Category:", mainCategory);
                    
                        // To iterate over subcategories within a main category
                        Object.keys(atcoder_categories[mainCategory]).forEach(subCategory => {

                            let subCategoryFull = `${mainCategory}_${subCategory}`;

                            console.log("  Subcategory: ",subCategory);
                            console.log("  SubcategoryFull: ",subCategoryFull);
                            console.log("  Checkbox_id: ",subcategory_checkbox_id)

                            if(subCategoryFull == subcategory_checkbox_id){
                                atcoder_categories[mainCategory][subCategory].forEach(problem => {
                                    console.log("    Problem:", problem);
                                    let problem_element = document.getElementById(problem);
                                    if (problem_element) { // Check if the element exists
                                        if (subcategory_checkbox.checked) {
                                            problem_element.classList.remove('not-selected-cell');
                                            problem_element.classList.add('selected-cell');
                                        } else {
                                            problem_element.classList.remove('selected-cell');
                                            problem_element.classList.add('not-selected-cell');
                                        }
                                    } else {
                                        console.error(`Element with id ${problem} not found.`);
                                    }
                                });
                            }

                        });
                    });
                })
                .catch(error => console.error('Error fetching JSON:', error));

            //Check subcategory
        });
    });
});
