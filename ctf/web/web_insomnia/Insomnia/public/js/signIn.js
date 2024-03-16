const apiEndpoint = "/index.php/login";

async function login() {
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
        password: password
      })
    })

    if (response.status === 200) {
      const jsonResponse = await response.json();

      document.cookie = `token=${jsonResponse.token}; path=/`;
      window.location.href = "/index.php/profile";
    } else if (response.status === 404) {
      const message = await response.text();
      alert(message);
    }


  } catch (error) {
    console.error("Error during login:", error);
  }
}