## GET请求：

请求url:http://127.0.0.1:8000/api/google/translate
请求参数：无
返回头类型：application/json
返回body内容：{"text":"I am still not happy!"}

## POST请求：

请求url:http://127.0.0.1:8000/api/user
请求头中Content-Type的值请设置为：application/json
请求body内容：
{"username":"随意输入username","password":"随意输入密码"}
返回头类型：Content-Type 为text/html; charset=utf-8
返回body内容：
注册成功则返回"Regist new user successfully!" status=200
注册失败返回"Duplicate Username" status=400
这个返回就并非返回json对象了，只是一个httpResponse,你根据状态码判定返回是成功失败即可，返回的message可以用于显示在页面提醒用户，或者让你了解是什么错误

## DELETE请求

请求url:http://127.0.0.1:8000/api/user/username (注意这里username是你自己填写的参数)
返回头类型：Content-Type 为text/html; charset=utf-8
返回body内容：
删除成功则返回"Deleted!" status=200
删除失败返回"This User did not exist" status=405
这个返回就并非返回json对象了，只是一个httpResponse,你根据状态码判定返回是成功失败即可，返回的message可以用于显示在页面提醒用户，或者让你了解是什么错误