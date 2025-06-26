#Exception Handling - Using, If condition, assert, try-except-finally, except exception

# ____________________________________________________________________

ItemsInCart = 5

# 1 -- If condition
if ItemsInCart != 4:        #  raise Exception("Product count not matching")
    pass                    # condition pass or fail - do nothing
# ____________________________________________________________________
# 2 -- assert
assert ItemsInCart == 4, "Product count not matching"
# ____________________________________________________________________
# 3 -- Try-Except-Finally
try:
    with open("test.txt", "r") as f:
        print(f.read())

except:
    print("File Not found")

# except Exception as e:
#     print(e)

# except FileNotFoundError:
#     print("File not found")

finally:
    print("File closed")        # Used just for reminder purpose