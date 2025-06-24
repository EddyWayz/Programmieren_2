window.addEventListener('DOMContentLoaded', () => {
    const btn = document.getElementById('theme-toggle');
    if (!btn) return;
    const saved = localStorage.getItem('theme');
    if (saved === 'dark') {
        document.body.classList.add('dark');
    } else {
        document.body.classList.add('light');
    }
    btn.addEventListener('click', () => {
        const nowDark = document.body.classList.toggle('dark');
        if (nowDark) {
            document.body.classList.remove('light');
        } else {
            document.body.classList.add('light');
        }
        localStorage.setItem('theme', nowDark ? 'dark' : 'light');
    });
});
