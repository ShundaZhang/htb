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
    <title>Document</title>
  </head>
  <body>
    <div class="app">
      <main>
        <section class="home" style="background-image: url(/images/theme.gif); height: 100vh;">
            <div class="home__container">
                <div class="home__title">
                    Welcome back <?= $username ?>
                </div>
                <div class="home__desc">
                    <?= $content ?>
                </div>
            </div>
            
        </section>
      </main>
      <footer></footer>
    </div>

  </body>
</html>
