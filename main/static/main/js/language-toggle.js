(function () {
  const KEY = "mt-lang";
  const root = document.documentElement;

  function currentLang() {
    return localStorage.getItem(KEY) || root.getAttribute("data-lang") || "fa";
  }

  function apply(lang) {
    document.querySelectorAll("[data-fa][data-en]").forEach((el) => {
      el.textContent = el.getAttribute("data-" + lang);
    });
    root.setAttribute("lang", lang === "fa" ? "fa" : "en");
    root.setAttribute("dir", lang === "fa" ? "rtl" : "ltr");
    root.setAttribute("data-lang", lang);
    localStorage.setItem(KEY, lang);

    const resumeLink = document.getElementById("resume-link");
    if (resumeLink) {
      const base = resumeLink.getAttribute("data-href");
      resumeLink.setAttribute("href", base + "?lang=" + lang);
    }
    const langBtn = document.getElementById("lang-toggle");
    if (langBtn) langBtn.textContent = lang === "fa" ? "English" : "فارسی";
  }

  function init() {
    apply(currentLang());
    const langBtn = document.getElementById("lang-toggle");
    if (langBtn) {
      langBtn.addEventListener("click", () => {
        apply(currentLang() === "fa" ? "en" : "fa");
      });
    }
  }

  document.addEventListener("DOMContentLoaded", init);
})();
