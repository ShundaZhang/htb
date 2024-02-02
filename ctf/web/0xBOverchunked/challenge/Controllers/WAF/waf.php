<?php
function waf_sql_injection($input)
{
    $sql_keywords = array(
        'SELECT',
        'INSERT',
        'UPDATE',
        'DELETE',
        'UNION',
        'DROP',
        'TRUNCATE',
        'ALTER',
        'CREATE',
        'FROM',
        'WHERE',
        'GROUP BY',
        'HAVING',
        'ORDER BY',
        'LIMIT',
        'OFFSET',
        'JOIN',
        'ON',
        'SET',
        'VALUES',
        'INDEX',
        'KEY',
        'PRIMARY',
        'FOREIGN',
        'REFERENCES',
        'TABLE',
        'VIEW',
        'AND',
        'OR',
        "'",
        '"',
        "')",
        '-- -',
        '#',
        '--',
        '-'
    );

    foreach ($sql_keywords as $keyword)
    {
        if (stripos($input, $keyword) !== false)
        {
            return false;
        }
    }
    return true;
}

?>
