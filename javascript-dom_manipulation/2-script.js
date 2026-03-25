document.addEventListener("DOMContentLoaded", () => {
  const trigger = document.querySelector("#red_header");
  const header = document.querySelector("header");

  trigger.addEventListener("click", () => {
    header.classList.add("red");
  });
});
