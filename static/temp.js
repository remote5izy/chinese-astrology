document.addEventListener("DOMContentLoaded", function () {
    const myform = document.getElementById("calculatorForm");

    myform.addEventListener("submit", async (e) => {
        e.preventDefault();
        const formData = new FormData(myform);

        const response = await fetch("/grace", {
            method: "POST",
            body: formData
        });

        const req = await response.json();

        console.log(req);

        const ans = document.getElementById("ans");
        console.log(ans); // This should now log the "ans" element

        // If you want to log the content of the "ans" element:
        console.log(ans.innerText);
    });
});
