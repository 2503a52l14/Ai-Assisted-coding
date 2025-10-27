// Display current year
document.getElementById('year').textContent = new Date().getFullYear();

// Handle contact form submit
function handleSubmit(e) {
  e.preventDefault();
  const fm = e.target;
  alert('Thanks ' + fm.name.value + '! Your message has been sent (demo only).');
  fm.reset();
}
