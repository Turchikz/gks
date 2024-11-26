let blocks = document.querySelectorAll(".reestr-form");
const myrange = ["#sel1 select", "#sel2 select", "#sel3 select"];
for (const el of myrange) {
  // проходим циклом по всем элементам объекта
  console.log(blocks[el]);
  let origSelect1 = document.querySelector(el);
  let options1 = [...origSelect1.options];
  origSelect1.addEventListener("change", () => {
    options1.forEach((option) => option.removeAttribute("selected"));
    options1[origSelect1.selectedIndex].setAttribute("selected", "");
  });
}

let birdForm1 = document.querySelectorAll("#sel1");

let birdForm2 = document.querySelectorAll("#sel2");

let birdForm3 = document.querySelectorAll("#sel3");
let container = document.querySelector("#form-container");
let addButton = document.querySelector("#add-form");
let totalForms = document.querySelector("#id_form-TOTAL_FORMS");

let formNum = birdForm1.length - 1;
addButton.addEventListener("click", addForm);

function addForm(e) {
  e.preventDefault();

  let newForm1 = birdForm1[0].cloneNode(true);
  let newForm2 = birdForm2[0].cloneNode(true);
  let newForm3 = birdForm3[0].cloneNode(true);
  let formRegex = RegExp(`form-(\\d){1}-`, "g");

  formNum++;
  newForm1.innerHTML = newForm1.innerHTML.replace(
    formRegex,
    `form-${formNum}-`
  );
  newForm2.innerHTML = newForm2.innerHTML.replace(
    formRegex,
    `form-${formNum}-`
  );
  newForm3.innerHTML = newForm3.innerHTML.replace(
    formRegex,
    `form-${formNum}-`
  );
  container.insertBefore(newForm1, addButton);
  container.insertBefore(newForm2, addButton);
  container.insertBefore(newForm3, addButton);

  totalForms.setAttribute("value", `${formNum + 1}`);
}
