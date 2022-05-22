/**
 * Creating dynamic formsets with Django and jQuery to allow 
 * adding of ingredients and instructions to recipes.
 * 
 * Credit: https://www.brennantymrak.com/articles/django-dynamic-formsets-javascript.html
 *  */

$(document).ready(() => {
    // check for the current number of forms then minus 1
    let ingredientFormNum = $('.ingredient-form').length-1;
    let instructionFormNum = $('.instruction-form').length-1;

    /**
     * Adds extra ingredient fields to the add recipe form to 
     * allow the connecting of multiple ingredients to one recipe.
     * 
     * @param {event} e - the button click event
     */
    $('#add-ingredient').on('click', (e) => {
        e.preventDefault();

        // clone the initial ingredient form
        let newForm = $('.ingredient-form:first').clone();
        // create regex object for updating new form html later
        let formRegex = RegExp(`form-(\\d){1}-`,'g');

        // increment formNum to create a unique-to-this-form integer
        ingredientFormNum++
        // update html using the earlier regex to update the for, name and id attributes
        newForm.html(newForm.html().replace(formRegex, 'form-' + ingredientFormNum + '-'));
        // add the new form as the last child in the fieldset
        newForm.appendTo('#ingredient-fieldset');

        // lastly, update Django's form management TOTAL_FORMS
        $('#ingredient-fieldset > #id_form-TOTAL_FORMS').attr('value', ingredientFormNum+1);
    });

    /**
     * Adds extra instruction fields to the add recipe form to 
     * allow the connecting of multiple instructions for one recipe.
     * 
     * @param {event} e - the button click event
     */
     $('#add-instruction').on('click', (e) => {
        e.preventDefault();

        // clone the initial instruction form
        let newForm = $('.instruction-form:first').clone();
        // create regex object for updating new form html later
        let formRegex = RegExp(`form-(\\d){1}-`,'g');

        // increment formNum to create a unique-to-this-form integer
        instructionFormNum++
        // update html using the earlier regex to update the for, name and id attributes
        newForm.html(newForm.html().replace(formRegex, 'form-' + instructionFormNum + '-'));
        // add the new form as the last child in the fieldset
        newForm.appendTo('#instruction-fieldset');

        // lastly, update Django's form management TOTAL_FORMS
        $('#instruction-fieldset > #id_form-TOTAL_FORMS').attr('value', instructionFormNum+1);
    });
});