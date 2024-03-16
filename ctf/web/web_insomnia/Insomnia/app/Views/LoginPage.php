<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <script
      src="/js/jquery-3.2.1.slim.min.js"
    ></script>
    <script
      src="/js/popper.min.js"
    ></script>
    <link rel="stylesheet" href="/css/style.css" />
    <title>Login</title>
    <script src="/js/signIn.js"></script>
  </head>
  <body>
    <div class="app">
    <header class="header">
        <ul class="menuItems">
          <li><a href="/" data-item="Home">Home</a></li>
          <li><a href="/index.php/login" >SignIn</a></li>
          <li><a href="/index.php/register" >SignUp</a></li>
        </ul>
      </header>
      <main>
        <section class="home" style="background-image: url(/images/theme.gif); height: 100vh;">
  <form class="home__container">
    <div class="home__title">
        Sign In
    </div>
    <div class="home__group">
        <label for="username">Username</label>
        <input id="username" type="email" name="username">
    </div>
    <div class="home__group">
        <label for="password">Password</label>
        <input id="password" type="password" name="password">
    </div>
    <div class="home__group">
        <div class="home__button" onclick="login()">
            Login now
        </div>
    </div>
</form>

        </section>
      </main>
      <footer></footer>
    </div>
    
  </body>
</html>
