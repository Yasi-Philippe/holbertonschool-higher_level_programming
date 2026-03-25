document.addEventListener("DOMContentLoaded", () => {
  const trigger = document.querySelector("#add_item");
  const list = document.querySelector(".my_list");


  trigger.addEventListener("click", () => {
    const newItem = document.createElement("li");
    newItem.textContent = "Item";
    list.appendChild(newItem);
  });
});
