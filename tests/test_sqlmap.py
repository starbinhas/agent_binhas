from tools import test_sql_injection

result = test_sql_injection("http://127.0.0.1:3000/rest/products/search?q=apple", "q")

print(result)