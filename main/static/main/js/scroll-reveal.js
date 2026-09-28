(function () {
  const DIA_COLOR = "var(--accent)";

  // TextAnimate (blur-in) for section titles
  const titles = document.querySelectorAll(".reveal-title");
  const titleObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-revealed");
          titleObserver.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.3 }
  );
  titles.forEach((t) => titleObserver.observe(t));

  // DiaTextReveal-style reveal for card titles, split by WORD (never by
  // individual character — Persian/Arabic script is cursive, so isolating
  // single letters in their own boxes breaks letter-joining and bidi
  // ordering, which visually looked like the whole word got reversed).
  // All words share one color and only stagger in with a slight delay.
  document.querySelectorAll(".dia-reveal").forEach((el) => {
    const text = el.textContent;
    const words = text.split(" ");
    el.textContent = "";
    el.setAttribute("aria-label", text);
    el.style.color = DIA_COLOR;
    words.forEach((word, i) => {
      const span = document.createElement("span");
      span.className = "dia-char";
      span.textContent = word;
      span.style.transitionDelay = i * 60 + "ms";
      el.appendChild(span);
      if (i < words.length - 1) el.appendChild(document.createTextNode(" "));
    });
  });

  // Reveal whole cards (fade/slide + trigger the dia text reveal) when scrolled into view
  const cards = document.querySelectorAll(".reveal-card");
  const cardObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-revealed");
          cardObserver.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.15 }
  );
  cards.forEach((c) => cardObserver.observe(c));
})();
