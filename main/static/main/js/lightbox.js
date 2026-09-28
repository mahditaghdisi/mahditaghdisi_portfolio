(function () {
  const modal = document.getElementById("lightbox-modal");
  const img = document.getElementById("lightbox-img");
  const closeBtn = document.getElementById("lightbox-close");
  if (!modal || !img) return;

  function open(src) {
    img.src = src;
    modal.hidden = false;
    requestAnimationFrame(() => modal.classList.add("is-open"));
  }
  function close() {
    modal.classList.remove("is-open");
    setTimeout(() => {
      modal.hidden = true;
      img.src = "";
    }, 200);
  }

  document.querySelectorAll("[data-lightbox-img]").forEach((btn) => {
    btn.addEventListener("click", () => open(btn.getAttribute("data-lightbox-img")));
  });
  if (closeBtn) closeBtn.addEventListener("click", close);
  modal.addEventListener("click", (e) => {
    if (e.target === modal) close();
  });
})();
