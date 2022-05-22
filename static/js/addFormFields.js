/**
 * Creating dynamic formsets with Django and JavaScript to allow adding of
 * extra ingredients to recipes.
 * 
 * Credit: https://www.brennantymrak.com/articles/django-dynamic-formsets-javascript.html
 *  */

// create variables from form elements.
let ingredientForm = document.querySelectorAll(".ingredient-form")
let container = document.querySelector("#form-container")
let addButton = document.querySelector("#add-form")
let totalForms = document.querySelector("#id_form-TOTAL_FORMS")
let formNum = ingredientForm.length-1

// add event listener on the relevant button.
addButton.addEventListener('click', addForm)

/**
 * Adds extra ingredient fields to the add recipe form to allow
 * the connecting of multiple ingredients to one recipe.
 * 
 * @param {event} e - prevents default button behaviour.
 */
function addForm(e){
    e.preventDefault()

    let newForm = ingredientForm[0].cloneNode(true)
    let formRegex = RegExp(`form-(\\d){1}-`,'g')

    formNum++
    newForm.innerHTML = newForm.innerHTML.replace(formRegex, `form-${formNum}-`)
    container.insertBefore(newForm, addButton)
    
    totalForms.setAttribute('value', `${formNum+1}`)
}