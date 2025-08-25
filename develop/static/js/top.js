// static/js/top.js
document.addEventListener('DOMContentLoaded', () => {
  console.log('top.js loaded');

  const mapRoot = document.querySelector('#japan_map');
  if (!mapRoot) return console.error('#japan_map が見つかりません');

  const svg = mapRoot.querySelector('svg');
  if (!svg) return console.error('SVGが見つかりません');

  // 都道府県のグループ要素を取得（g.prefecture または path.prefecture）
  const groups = Array.from(svg.querySelectorAll('.prefecture'))
    .map(el => el.closest('.prefecture') || el);
  const uniq = [...new Set(groups)];

  uniq.forEach(pref => {
    const paint = (color) =>
      pref.querySelectorAll('path,polygon').forEach(p => p.style.fill = color);

    pref.addEventListener('mouseenter', () => paint('#ff0000'));
    pref.addEventListener('mouseleave', () => paint(''));
  });
});



// モーダル
document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll('[data-code]').forEach(region => {
        region.addEventListener('click', () => {
            const prefId = region.getAttribute('data-code');  // ← svgの属性に合わせる

            fetch(`/get_board_image/${prefId}`)
                .then(res => res.json())
                .then(data => {
                    const modal = document.getElementById('board-modal');
                    const container = document.getElementById('board-image-container');
                    container.innerHTML = '';

                    if (data.image_path) {
                        const img = document.createElement('img');
                        img.src = `/${data.image_path}`;
                        img.alt = "回覧板画像";
                        container.appendChild(img);
                    } else {
                        container.innerHTML = "<p>回覧板がありません。</p>";
                    }

                    modal.classList.remove('hidden');
                });
        });
    });

    // モーダル閉じる
    document.querySelector(".close-button").addEventListener("click", () => {
        document.getElementById("board-modal").classList.add("hidden");
    });

    document.getElementById("board-modal").addEventListener("click", (e) => {
        if (e.target.id === "board-modal") {
            e.target.classList.add("hidden");
        }
    });
});

