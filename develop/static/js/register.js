function login() {
  const username = document.getElementById('username').value;
  const password = document.getElementById('password').value;

  // 簡単なダミーチェック（実際はサーバー側で認証処理）
  if (username === 'admin' && password === 'password') {
    alert('ログイン成功');
  } else {
    alert('ユーザー名またはパスワードが違います');
  }

  return false; // フォーム送信を止める
}
