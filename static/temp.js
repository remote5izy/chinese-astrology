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

    const mingGongItem = req.find(item => item.includes("命宮"));

    if (mingGongItem) {
        // 取得 "命宮" 後的其他元素，並過濾值為 0 的元素
        const mingGongIndex = mingGongItem.indexOf("命宮");
        const elementsAfterMingGong = mingGongItem.slice(mingGongIndex + 1);

        // 取得最後兩個元素
        const lastTwoElements = elementsAfterMingGong.slice(-2);

        // 檢查最後兩個元素是否非0
        if (lastTwoElements.every(value => value !== 0)) {
            ans.innerText += `${lastTwoElements.join(',')}坐命\n`;
        } else {
            ans.innerText += "命宮無主星\n";
        }
    }
});