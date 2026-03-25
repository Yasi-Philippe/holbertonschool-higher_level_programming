document.addEventListener("DOMContentLoaded", () => {
  const trigger = document.querySelector("#update_header");
  const my_header = document.querySelector("header");

  trigger.addEventListener("click", () => {
    my_header.textContent = "New Header!!!";
  });
});
