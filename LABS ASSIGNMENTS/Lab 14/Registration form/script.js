const form = document.getElementById("registrationForm");

form.addEventListener("input", validateField);
form.addEventListener("submit", handleSubmit);

function validateField(e) {
  const field = e.target;
  const errorMsg = field.parentElement.querySelector(".error");

  if (field.id === "name") {
    errorMsg.textContent = field.value.trim().length < 3 ? "Name must be at least 3 characters." : "";
  }

  if (field.id === "email") {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    errorMsg.textContent = !emailRegex.test(field.value.trim()) ? "Invalid email format." : "";
  }

  if (field.id === "phone") {
    const phoneRegex = /^[0-9]{10}$/;
    errorMsg.textContent = !phoneRegex.test(field.value.trim()) ? "Phone must be 10 digits." : "";
  }

  if (field.id === "dept" || field.id === "event") {
    errorMsg.textContent = field.value === "" ? "Please select an option." : "";
  }
}

function handleSubmit(e) {
  e.preventDefault();
  let valid = true;

  form.querySelectorAll("input, select").forEach((field) => {
    const event = new Event("input");
    field.dispatchEvent(event);
    const error = field.parentElement.querySelector(".error").textContent;
    if (error) valid = false;
  });

  if (valid) {
    alert("🎉 Registration successful! Welcome to SRU Tech Fest 2025!");
    form.reset();
  } else {
    alert("⚠️ Please fix the highlighted errors before submitting.");
  }
}
