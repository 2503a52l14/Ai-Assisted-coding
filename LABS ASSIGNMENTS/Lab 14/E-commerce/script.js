let cartCount = 0;

const cartDisplay = document.getElementById("cart-count");
const addButtons = document.querySelectorAll(".add-to-cart");

addButtons.forEach(button => {
  button.addEventListener("click", () => {
    cartCount++;
    cartDisplay.textContent = cartCount;

    // Add small animation to cart when item is added
    cartDisplay.style.transform = "scale(1.3)";
    cartDisplay.style.transition = "transform 0.2s ease";

    setTimeout(() => {
      cartDisplay.style.transform = "scale(1)";
    }, 200);
  });
});
