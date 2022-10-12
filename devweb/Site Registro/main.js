function setFormMessage(formElement, type, message) {
    const messageElement = formElement.querySelector(".formMessage");

    messageElement.textContent = message;
    messageElement.classList.remove("formMessageSuccess", "formMessageError");
    messageElement.classList.add(`formMessage${type}`);
}

function setInputError(inputElement, message) {
    inputElement.classList.add("formInputError");
    inputElement.parentElement.querySelector(".formInputErrorMessage").textContent = message;
}

function clearInputError(inputElement) {
    inputElement.classList.remove("formInputError");
    inputElement.parentElement.querySelector(".formInputErrorMessage").textContent = "";
}

document.addEventListener("DOMContentLoaded", () => {
    const loginForm = document.querySelector("#login");
    const createAccountForm = document.querySelector("#createAccount");

    document.querySelector("#linkCreateAccount").addEventListener("click", e => {
        e.preventDefault();
        loginForm.classList.add("formHidden");
        createAccountForm.classList.remove("formHidden");
    });

    document.querySelector("#linkLogin").addEventListener("click", e => {
        e.preventDefault();
        loginForm.classList.remove("formHidden");
        createAccountForm.classList.add("formHidden");
    });

    loginForm.addEventListener("submit", e => {
        e.preventDefault();
        setFormMessage(loginForm, "Error", "Nome de usuário ou senha inválidos");
    });

    document.querySelectorAll(".formInput").forEach(inputElement => {
        inputElement.addEventListener("blur", e => {
            if (e.target.id === "signupUsername")
            {
                if(e.target.value.length <= 0) {setInputError(inputElement, "O nome de usuário não pode estar em branco!");}
                else if (e.target.value.length < 5) {setInputError(inputElement, "O nome de usuário precisa ter mais do que 5 caracteres!");}
            }

            else if (e.target.id === "email")
            {
                let emailString0 = "@"
                let emailString1 = ".com";
                if (!e.target.value.includes(emailString0) || !e.target.value.includes(emailString1)) {setInputError(inputElement, "Endereço de e-mail inválido");}
            }
        });

        inputElement.addEventListener("input", e => {
            clearInputError(inputElement);
        });
    });

    createAccountForm.addEventListener("submit", e => {
        e.preventDefault();
    });
});