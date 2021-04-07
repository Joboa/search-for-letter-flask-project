import sys

try:
    1/0

# except:
#     err = sys.exc_info()
#     for e in err:
#         print(e)

except Exception as err:
    print(str(err))


# try:
#     with open('file.txt') as fh:
#         file_data = fh.read()
#     print(file_data)

# # except FileNotFoundError:
# #     print('file not found')
# except PermissionError:
#     print('not allowed')
# except Exception as err:
#     print('Some othe error occured', str(err))
