'''
Name: 
Description:
Bugs: For example "Fails under x parameters"
Features: 
Sources: 
Log: 1
'''
data = input("Enter the data as 'Length, Height, Width:  ")
print(data)
dimensions = data.split(',')
print(dimensions)
print(dimensions[0])
# def get_type(length, height, width):
#     if 3.5 <= length <= 4.25 and 3.5 <= height <= 6 and .007 <= width <= .016:
#         type = 'reg_post_card'
#     elif length > 4.25 and length < 6:
#         type = 'large_post_card'
#     elif 