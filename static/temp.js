const myform = document.getElementById("calculatorForm");

myform.addEventListener("submit", async (e) => {
    e.preventDefault();
    const formData = new FormData(myform);


    const response =
        await fetch("/grace", {
            method: "POST",
            body: formData
        });

    const req = await response.json();

    console.log(req);

    const ans = document.getElementById("ans");
    ans.innerText += JSON.stringify(req);
});