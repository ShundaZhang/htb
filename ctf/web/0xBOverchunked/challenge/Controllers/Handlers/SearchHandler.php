<?php
require_once '../Database/Cursor.php';
require_once '../WAF/waf.php';

if (isset($_SERVER["HTTP_TRANSFER_ENCODING"]) && $_SERVER["HTTP_TRANSFER_ENCODING"] == "chunked")
{
    $search = $_POST['search'];

    $result = unsafequery($pdo, $search);

    if ($result)
    {
        echo "<div class='results'>No post id found.</div>";
    }
    else
    {
        http_response_code(500);
        echo "Internal Server Error";
        exit();
    }

}
else
{
    if ((isset($_POST["search"])))
    {
        $search = $_POST["search"];
        if (waf_sql_injection($search))
        {
            $result = safequery($pdo, $search);
            if ($result)
            {
                echo '
                    <div class="grid-container">
                    <div class="grid-item">
                        <img class="post-logo" src="../../assets/images/posts/' . $result["image"] . '" width="100">
                    </div>
                    <div class="grid-item">
                        <p><font color="#F44336">Name</font>: ' . $result["gamename"] . '</p>
                        <p><font color="#F44336">Description</font>: ' . $result["gamedesc"] . '</p>
                    </div>
                    </div>';
            }
            else
            {
                echo "<div class='results'>No post id found.</div>";
            }
        }
        else
        {
            echo "<div class='results'>SQL Injection attempt identified and prevented by WAF!</div>";
        }
    }
    else
    {
        echo "<div class='results'>Unsupported method!</div>";
        http_response_code(400);
    }

}

?>
