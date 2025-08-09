document.addEventListener("DOMContentLoaded", function () {
  const toggleBtn = document.getElementById("toggleBtn");
  const sidebar = document.getElementById("sidebar");

  // Sidebar toggle
  toggleBtn.addEventListener("click", function () {
    sidebar.classList.toggle("active");
  });

  // Smooth Scroll with easing
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (!target) return;

      // Custom smooth animation
      const startPos = window.pageYOffset;
      const targetPos = target.getBoundingClientRect().top + window.pageYOffset;
      const distance = targetPos - startPos;
      const duration = 800; // animation speed in ms
      let startTime = null;

      function animation(currentTime) {
        if (startTime === null) startTime = currentTime;
        const timeElapsed = currentTime - startTime;
        const run = easeInOutCubic(timeElapsed, startPos, distance, duration);
        window.scrollTo(0, run);
        if (timeElapsed < duration) requestAnimationFrame(animation);
      }

      // Easing function for smooth glassy feel
      function easeInOutCubic(t, b, c, d) {
        t /= d / 2;
        if (t < 1) return (c / 2) * t * t * t + b;
        t -= 2;
        return (c / 2) * (t * t * t + 2) + b;
      }s

      requestAnimationFrame(animation);
    });
  });
});
/* Toggle Light/Dark Theame */
document.addEventListener("DOMContentLoaded", () => {
  const themeToggle = document.getElementById("theme-toggle");
  const root = document.documentElement;

  // Define icons for dark and light modes
  const darkIcon = "/static/assets/Theme_Toggle_Dark.svg";  // replace with your dark mode icon path
  const lightIcon = "/static/assets/Theme_Toggle_Light.svg"; // replace with your light mode icon path

  // Initialize theme and icon from localStorage or default dark
  let savedTheme = localStorage.getItem("theme") || "light";
  root.setAttribute("data-theme", savedTheme);
  updateIcon(savedTheme);

  themeToggle.addEventListener("click", () => {
    let currentTheme = root.getAttribute("data-theme");
    let newTheme = currentTheme === "light" ? "dark" : "light";
    root.setAttribute("data-theme", newTheme);
    localStorage.setItem("theme", newTheme);
    updateIcon(newTheme);
  });

  function updateIcon(theme) {
    const img = themeToggle.querySelector("img");
    if (theme === "light") {
      img.src = lightIcon;
      img.alt = "Switch to Dark Mode";
    } else {
      img.src = darkIcon;
      img.alt = "Switch to Light Mode";
    }
  }
});



