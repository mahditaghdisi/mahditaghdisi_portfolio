(function () {
  const dock = document.getElementById("site-dock");
  if (!dock) return;
  const icons = Array.from(dock.querySelectorAll(".dock-icon"));

  function magnify(e) {
    const mx = e ? e.clientX : null;
    icons.forEach((icon) => {
      if (mx === null) {
        icon.style.transform = "";
        return;
      }
      const rect = icon.getBoundingClientRect();
      const center = rect.left + rect.width / 2;
      const dist = Math.abs(mx - center);
      const scale = Math.max(1, 1.55 - dist / 110);
      icon.style.transform = `translateY(${(scale - 1) * -10}px) scale(${scale})`;
    });
  }

  dock.addEventListener("mousemove", magnify);
  dock.addEventListener("mouseleave", () => magnify(null));
})();
