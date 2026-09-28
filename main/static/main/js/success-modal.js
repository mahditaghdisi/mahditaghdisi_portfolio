(function () {
  const form = document.getElementById("contact-form");
  const modal = document.getElementById("success-modal");
  const okBtn = document.getElementById("success-modal-ok");
  if (!form || !modal) return;

  function openModal() {
    modal.hidden = false;
    requestAnimationFrame(() => modal.classList.add("is-open"));
  }
  function closeModal() {
    modal.classList.remove("is-open");
    setTimeout(() => (modal.hidden = true), 200);
  }

  if (form.dataset.success === "1") {
    openModal();
  }
  if (okBtn) okBtn.addEventListener("click", closeModal);
  modal.addEventListener("click", (e) => {
    if (e.target === modal) closeModal();
  });
})();
