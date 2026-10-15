/* ===== Settings: fill these in before launch ===== */
const WHATSAPP_NUMBER = ""; // country code + number, no + or spaces, e.g. "971500000000"
const CONTACT_EMAIL = "";   // e.g. "hello@yourdomain.com"

const $ = (s, el = document) => el.querySelector(s);
const $$ = (s, el = document) => [...el.querySelectorAll(s)];
const reduceMotion = matchMedia("(prefers-reduced-motion: reduce)").matches;

/* ----- Header: solid background after scrolling ----- */
const header = $(".header");
const actionbar = $(".actionbar");
function onScroll() {
  const y = window.scrollY;
  header && header.classList.toggle("is-solid", y > 24);
  actionbar && actionbar.classList.toggle("is-shown", y > window.innerHeight * 0.6);
}
addEventListener("scroll", onScroll, { passive: true });
onScroll();

/* ----- Mobile drawer ----- */
const burger = $(".burger");
const drawer = $("#drawer");
function setDrawer(open) {
  if (!burger || !drawer) return;
  burger.setAttribute("aria-expanded", String(open));
  burger.setAttribute("aria-label", open ? "Close menu" : "Open menu");
  drawer.classList.toggle("is-open", open);
  drawer.toggleAttribute("inert", !open);
  document.documentElement.style.overflow = open ? "hidden" : "";
  if (open) setTimeout(() => $("a", drawer)?.focus({ preventScroll: true }), 250);
}
if (burger && drawer) {
  drawer.setAttribute("inert", "");
  burger.addEventListener("click", () => setDrawer(burger.getAttribute("aria-expanded") !== "true"));
  $$("a", drawer).forEach(a => a.addEventListener("click", () => setDrawer(false)));
  addEventListener("keydown", e => { if (e.key === "Escape" && drawer.classList.contains("is-open")) { setDrawer(false); burger.focus(); } });
  matchMedia("(min-width: 921px)").addEventListener("change", e => { if (e.matches) setDrawer(false); });
}

/* ----- WhatsApp links ----- */
$$("[data-wa]").forEach(a => {
  if (WHATSAPP_NUMBER) {
    a.href = `https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent("Hi Ilinka, I'd like to book a consultation about investing in Dubai.")}`;
    a.target = "_blank";
    a.rel = "noopener";
  }
});

/* ----- Yield calculator ----- */
const calc = $("#calc");
if (calc) {
  const MAX = 12;
  const val = id => parseFloat($(id).value) || 0;
  const pct = n => (Number.isFinite(n) ? n.toFixed(1) : "0.0") + "%";
  const aed = n => "AED " + Math.round(n).toLocaleString("en-US");
  const fill = v => 100 - (Math.max(0, Math.min(v, MAX)) / MAX) * 100;
  function update() {
    const price = val("#price"), rent = val("#rent"), costs = val("#costs");
    const gross = price ? (rent / price) * 100 : 0;
    const netIncome = rent - costs;
    const net = price ? (netIncome / price) * 100 : 0;
    $("#netYield").textContent = pct(net);
    $("#grossYield").textContent = pct(gross);
    $("#netIncome").textContent = aed(netIncome);
    $("#dGross").style.strokeDashoffset = fill(gross);
    $("#dNet").style.strokeDashoffset = fill(net);
  }
  $$("input", calc).forEach(i => i.addEventListener("input", update));
  update();
}

/* ----- Consultation form (WhatsApp or email, no server needed) ----- */
const form = $("#consultForm");
if (form) {
  form.addEventListener("submit", e => {
    e.preventDefault();
    const note = $("#formNote");
    if (!form.checkValidity()) { form.reportValidity(); return; }
    const d = new FormData(form);
    const msg = [
      "New consultation request",
      `Name: ${d.get("name")}`,
      `Email: ${d.get("email")}`,
      `Budget: ${d.get("budget")}`,
      `Goal: ${d.get("goal")}`,
      `Message: ${d.get("message") || "None"}`
    ].join("\n");
    if (WHATSAPP_NUMBER) {
      window.open(`https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(msg)}`, "_blank", "noopener");
      note.textContent = "WhatsApp is opening with your request. Press send to finish.";
    } else if (CONTACT_EMAIL) {
      location.href = `mailto:${CONTACT_EMAIL}?subject=${encodeURIComponent("Consultation request")}&body=${encodeURIComponent(msg)}`;
      note.textContent = "Your email app is opening with your request. Press send to finish.";
    } else {
      note.textContent = "Thank you. Ilinka will reply to arrange your consultation.";
    }
    form.reset();
  });
}

/* ----- Custom cursor: a small arch that follows the pointer ----- */
(function cursor() {
  const fine = matchMedia("(hover: hover) and (pointer: fine)").matches;
  const el = $(".cursor");
  if (!fine || !el) return;
  document.documentElement.classList.add("has-cursor");
  const arch = $(".cursor-arch", el), dot = $(".cursor-dot", el), label = $(".cursor-label", el);
  let x = innerWidth / 2, y = innerHeight / 2, ax = x, ay = y;
  addEventListener("pointermove", e => { x = e.clientX; y = e.clientY; el.classList.remove("is-hidden"); }, { passive: true });
  document.addEventListener("pointerleave", () => el.classList.add("is-hidden"));
  addEventListener("blur", () => el.classList.add("is-hidden"));
  function frame() {
    const k = reduceMotion ? 1 : 0.2;
    ax += (x - ax) * k; ay += (y - ay) * k;
    arch.style.left = ax + "px"; arch.style.top = ay + "px";
    label.style.left = ax + "px"; label.style.top = ay + "px";
    dot.style.left = x + "px"; dot.style.top = y + "px";
    requestAnimationFrame(frame);
  }
  frame();
  addEventListener("pointerover", e => {
    const t = e.target;
    const view = t.closest("[data-cursor]");
    const text = t.closest("input, textarea, [contenteditable]");
    const link = t.closest("a, button, summary, select, label");
    el.classList.toggle("is-view", !!view);
    el.classList.toggle("is-text", !!text);
    el.classList.toggle("is-link", !!link && !view && !text);
    label.textContent = view ? view.dataset.cursor : "";
  });
  addEventListener("pointerdown", () => arch.animate([{ scale: 1 }, { scale: 0.85 }, { scale: 1 }], { duration: 300 }));
})();

const yr = $("#year");
if (yr) yr.textContent = new Date().getFullYear();
