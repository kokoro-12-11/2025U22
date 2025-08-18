document.addEventListener("DOMContentLoaded", () => {
    const aiButton = document.getElementById("ai_button");
    const contentInput = document.getElementById("content"); // 質問内容の input

    aiButton.addEventListener("click", async () => {
        try {
            const res = await fetch("/board_create", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({})
            });

            if (!res.ok) throw new Error(`HTTPエラー: ${res.status}`);

            const data = await res.json();
            contentInput.value = data.answer; // input に AI回答をセット

        } catch (err) {
            console.error(err);
            contentInput.value = `エラーが発生しました:\n${err}`;
        }
    });
});
