<html>
    <body>
        <?php if (isset($_GET['html'])): ?>
            <?php echo $_GET['html']; ?>
        <?php else: ?>
            <h1>HTML Tester</h1>
            <p>Internal development tool</p>
            <form action="index.php" method="get">
                <input type="text" name="html" />
                <input type="submit" value="Submit" />
            </form>
        <?php endif; ?>
    </body>
</html>