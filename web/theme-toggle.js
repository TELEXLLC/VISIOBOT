const btn = document.getElementById('theme-toggle');
btn.onclick = () => {
  document.body.classList.toggle('dark');
  btn.innerText = document.body.classList.contains('dark') ? "🌙" : "☀️";
};