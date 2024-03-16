const apiEndpoint = "/index.php/register";

async function register() {
  const usernameInput = document.querySelector("#username");
  const passwordInput = document.querySelector("#password");

  const username = usernameInput.value;
  const password = passwordInput.value;
  console.log(username, password);
  try {
    const response = await fetch(apiEndpoint, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        username: username,
        password: password,
      }),
    });

    if (response.status === 200) {
      alert(await response.text());

      setTimeout(() => {
        window.location.href = "/index.php/login";
      }, 1000);
    } else {
      const message = await response.text();
      alert(message);
    }
  } catch (error) {
    console.error("Error during login:", error);
  }
}