import f, lps, psn, psw

if f.test() and lps.test() and psn.test() and psw.test(): print('All scripts loaded.')
else: print('An error ocurred.'), exit()

print('Please do not use this toolkit in a way which harasses the 1990 Computer Misuse Act.\nThis toolkit only has over-simple/basic tools and there are also lots of bugs, as this is the developer\'s first time writing full code, sorry.') 
userscmd = str(input('chaos>>> '))

try: f.process_cmd(userscmd) 
except BaseException as e: print(f'Toolkit closed down. Reason:{e.args}')
