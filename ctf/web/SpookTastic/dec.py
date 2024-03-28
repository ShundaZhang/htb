'''
https://github.com/hackthebox/htboo-ctf-2023/tree/main/htboo-ctf-2023/web/%5BVery%20Easy%5D%20SpookTastic

XSS exploitation
When the function start_bot is called and the browser loads up the bot.html template, it renders the provided data using unsafe string escaping that can be noticed by the |safe operator.

bot.html
{% for email in emails %}
    <span>{{ email|safe }}</span><br/>
{% endfor %}
We can leverage this by causing xss and popping an alert, which will cause the flag to be sent to us via websocket connection.

But we first must bypass the blacklist_pass function.

This can be done by using an xss payload that does not use the script tag to achieve javascript execution, such as this example that uses an img tag:

<img src=0 onerror=alert(0) />

HTB{al3rt5_c4n_4nd_w1l1_c4us3_jumpsc4r35!!}
'''
