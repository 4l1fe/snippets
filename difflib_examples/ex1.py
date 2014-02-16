import difflib

#pprint(inspect.getmembers(, inspect.isfunction))
diff_c = difflib.Differ()
rfc2068_file = open('rfc2068.html')
rfc2068_lines = rfc2068_file.readlines()
rfc2616_file = open('rfc2616.html')
rfc2616_lines = rfc2616_file.readlines()
diff = diff_c.compare(rfc2068_lines, rfc2616_lines)
for i in diff: print(i)