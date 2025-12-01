#calculator program
# 🎯 Step 1: Take two numbers from the user
num1=float(input('✏️ Type Your First Number Please----> ').strip())
num2=float(input('✏️ Type Your second Number Please----> ').strip())
# 🎯 Step 2: Ask user if they want to update numbers or continue
choice=input(f'📝 You Choose {num1} and {num2} if you want to update them type U or to continue type C : ').strip().upper()
if choice=='U':
    num1=float(input('✏️ Type Your First Number Please----> ').strip())
    num2=float(input('✏️ Type Your second Number Please----> ').strip())
    print(f'✔️\nYour Numbers Updated Successfully to {num1} and {num2}')
elif choice=='C':
    print(f'🏃\nYou Continue with {num1} and {num2}')
else:
    print('🚨\nInvalid Input Please Try Again Later')
# 🎯 Step 3: Display available operations
print('‧₊˚✧✧˚₊‧\nAvailable Operations :\n+\n-\n*\n/\n%\n//\n**\n q for quit‧₊˚✧✧˚₊‧')
operation=input('👆 Please Choose One Operations from the Above----> ').strip()
# 🔁 Loop until user chooses to quit 'q'
while operation != 'q':
    if operation=='+':
        result=num1+num2
        print(f'💡 The Result of {num1} + {num2} = {result}')
    elif operation=='-':
        result=num1-num2
        print(f'💡 The Result of {num1} - {num2} = {result}')
    elif operation=='*':
        result=num1*num2
        print(f'💡 The Result of {num1} * {num2} = {result}')
    elif operation=='/':
        if num2 !=0:
            result=num1/num2
            print(f'💡 The Result of {num1} / {num2} = {result}')
        # ⚠️ Handle division by zero case
        else:
            print('🚨\nError: Division by zero is not allowed.')
    elif operation=='%':
        result=num1%num2
        print(f'💡 The Result of {num1} % {num2} = {result}')
    elif operation=='//':
        result=num1//num2
        print(f'💡 The Result of {num1} // {num2} = {result}')
    elif operation=='**':
        result=num1**num2
        print(f'💡 The Result of {num1} ** {num2} = {result}')
    else:
        print('🚨 Invalid Operation Please Try Again Later')
    operation=input('👆 Please Choose Another Operation or type q to quit----> ').strip()
print('👋 Thank You for Using Our Calculator. Goodbye!')
