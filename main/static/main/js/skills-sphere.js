(function () {
  const wrap = document.getElementById("skills-sphere");
  if (!wrap) return;

  const words = JSON.parse(wrap.getAttribute("data-skills") || "[]");
  const radius = 130;
  const count = words.length;

  const nodes = words.map((word, i) => {
    // Fibonacci sphere distribution for even spacing
    const y = 1 - (i / (count - 1)) * 2;
    const r = Math.sqrt(1 - y * y);
    const theta = (Math.PI * (3 - Math.sqrt(5))) * i;
    const x = Math.cos(theta) * r;
    const z = Math.sin(theta) * r;

    const el = document.createElement("span");
    el.className = "sphere-tag";
    el.textContent = word;
    el.dataset.x = x;
    el.dataset.y = y;
    el.dataset.z = z;
    wrap.appendChild(el);
    return el;
  });

  let rotY = 0;
  let rotX = 0.15;
  let dragging = false;
  let lastX = 0, lastY = 0;
  let autoSpin = true;

  function render() {
    nodes.forEach((el) => {
      const x = parseFloat(el.dataset.x);
      const y = parseFloat(el.dataset.y);
      const z = parseFloat(el.dataset.z);

      // rotate around Y then X
      const cosY = Math.cos(rotY), sinY = Math.sin(rotY);
      const x1 = x * cosY - z * sinY;
      const z1 = x * sinY + z * cosY;

      const cosX = Math.cos(rotX), sinX = Math.sin(rotX);
      const y1 = y * cosX - z1 * sinX;
      const z2 = y * sinX + z1 * cosX;

      const scale = (z2 + 2) / 3;
      const opacity = 0.35 + scale * 0.65;

      el.style.transform =
        `translate(-50%, -50%) translate3d(${x1 * radius}px, ${y1 * radius}px, ${z2 * radius}px) scale(${scale})`;
      el.style.opacity = opacity;
      el.style.zIndex = Math.round(scale * 100);
    });
  }

  function loop() {
    if (autoSpin && !dragging) {
      rotY += 0.0035;
    }
    render();
    requestAnimationFrame(loop);
  }

  wrap.addEventListener("pointerdown", (e) => {
    dragging = true;
    lastX = e.clientX;
    lastY = e.clientY;
  });
  window.addEventListener("pointerup", () => (dragging = false));
  window.addEventListener("pointermove", (e) => {
    if (!dragging) return;
    const dx = e.clientX - lastX;
    const dy = e.clientY - lastY;
    rotY += dx * 0.006;
    rotX += dy * 0.006;
    rotX = Math.max(-1.1, Math.min(1.1, rotX));
    lastX = e.clientX;
    lastY = e.clientY;
  });

  requestAnimationFrame(loop);
})();
