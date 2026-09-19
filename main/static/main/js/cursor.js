(function () {
  if (window.matchMedia("(pointer: coarse)").matches) return;

  const cursor = document.createElement("div");
  cursor.id = "smooth-cursor";
  document.body.appendChild(cursor);

  let mx = window.innerWidth / 2, my = window.innerHeight / 2;
  let cx = mx, cy = my;
  const ease = 0.18;

  window.addEventListener("mousemove", (e) => {
    mx = e.clientX;
    my = e.clientY;
  });

  document.addEventListener("mousedown", () => cursor.classList.add("is-active"));
  document.addEventListener("mouseup", () => cursor.classList.remove("is-active"));

  document.querySelectorAll("a, button, .pill-btn, input, textarea, [role='button']").forEach((el) => {
    el.addEventListener("mouseenter", () => cursor.classList.add("is-active"));
    el.addEventListener("mouseleave", () => cursor.classList.remove("is-active"));
  });

  function tick() {
    cx += (mx - cx) * ease;
    cy += (my - cy) * ease;
    cursor.style.transform = `translate(${cx}px, ${cy}px) translate(-50%, -50%)`;
    requestAnimationFrame(tick);
  }
  requestAnimationFrame(tick);
})();
