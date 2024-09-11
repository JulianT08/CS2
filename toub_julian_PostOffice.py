'''
Name: 
Description:
Bugs: For example "Fails under x parameters"
Features: 
Sources: 
Log: 1
'''
while True:
    data = input("Enter the data as 'Length, Height, Width, Starting Zip Code, Ending Zip Code:  ")
    dimensions = data.split(',')                                #splits the data inputted by the user into length, height, and width, based on index
    length = float(dimensions[0])                               #sets the variable 'lenght' = to the first user input
    height = float(dimensions[1])                               #sets the variable 'height' = to the second user input                                      
    width = float(dimensions[2])                                #sets the variable 'width' = to the third user input
    zip_start = int(dimensions[3]                               )#sets the variable 'zip_start' = to the fourth user input
    zip_end = int(dimensions[4])                                #sets the variable 'zip_end' = to the fifth user input
    
    if length < 0:
        print('Length cannot be negative.')                     #checks to see if the input 'length' is negative. if it is, the loop will require that the data is re-entered
    elif height < 0:
        print('Height cannot be negative.')                     #checks to see if the input 'height' is negative. if it is, the loop will require that the data is re-entered 
    elif width < 0:
        print('Width cannot be negative.')                      #checks to see if the input 'width' is negative. if it is, the loop will require that the data is re-entered
    else:                                                       #if all variables check out (not negative), the code will proceed. 
        break

print(f'L: {length} H: {height} W: {width}')                    #prints the user's dimensions back to them
def get_type(length, height, width):
    '''
    Determines the type of package that the user would like to ship. 

    Args:
        length (float): The length of one side of the package.
        height (float): The height of the package.
        width (float): The width or thickness of the package.
    
    Returns:
        type (str): The type of package.
    
    Raises:
        none

    '''
    if 3.5 <= length <= 4.25 and 3.5 <= height <= 6 and .007 <= width <= .016:
        type = 'reg_post_card'
    elif 4.25 < length < 6 and 6 < height < 11 and .016 < width < .25:
        type = 'large_post_card'
    elif 3.5 <= length <= 6.125 and 5 <= height <= 11.5 and .016 <= width <= .25:
        type = 'envelope'
    elif 6.125 < length < 24 and 11 <= height <= 18 and .25 <= width <= .5:
        type = 'large_envelope'
    elif length >= 24 and width > 18 and width >.5 and (length*2) + (width*2) <= 84:
        type = 'package'
    elif length >= 24 and width > 18 and width >.5 and 84 < (length*2) + (width*2) < 130:
        type = 'large_package'
    
    else:
        type = 'unmailable'
        print('This package is unmailable')
    return(type)
#def get_zone(zip_start, zip_end):
#    zone1 <= 
def main():
    type = get_type(length, height, width)
    print(f'Your shipment is a {type}. ')

if __name__ == "__main__":
    main()
