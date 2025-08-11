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
