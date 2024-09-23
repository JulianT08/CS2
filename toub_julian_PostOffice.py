'''
Name: 
Description:
Bugs: For example "Fails under x parameters"
Features: 
Sources: 
Log: 1
'''

def get_postage_type(length, height, width):
    '''
    Determines the postage_type of package that the user would like to ship. 

    Args:
        length (float): The length of one side of the package.
        height (float): The height of the package.
        width (float): The width or thickness of the package.

    Returns:
        postage_type (str): The postage_type of package.

    Raises:
        none
    '''
    if 3.5 <= length <= 4.25 and 3.5 <= height <= 6 and .007 <= width <= .016:
        return 'reg_post_card'
    elif 4.25 < length < 6 and 6 < height < 11 and .007 <= width <= .015:
        return 'large_post_card'
    elif 3.5 <= length <= 6.125 and 5 <= height <= 11.5 and .016 < width < .25:
        return 'envelope'
    elif 6.125 < length < 24 and 11 <= height <= 18 and .25 <= width <= .5:
        return 'large_envelope'
    elif length >= 24 and width >.5 and length + (height*2) + (width*2) <= 84:
        return 'package'
    elif 84 < length + (length*2) + (width*2) < 130:
        return 'large_package'

    else:
        return 'unmailable'
def get_zone(zip_code):
    if 1 <= zip_code <= 6999:
        return 1
    elif 7000 <= zip_code <= 19999:
        return 2
    elif 20000 <= zip_code <= 35999:
        return 3
    elif 36000 <= zip_code <= 62999:
        return 4
    elif 63000 <= zip_code <= 84999:
        return 5
    elif 85000 <= zip_code <= 99999:
        return 6
    else:
        return None
def calculate_cost(postage_type, distance):
    if postage_type == "reg_post_card":
        return .20 + .03 * distance
    elif postage_type == "large_post_card":
        return .37 + .03 * distance
    elif postage_type == "envelope":
        return .37 + .04 * distance
    elif postage_type == "large_envelope":
        return .60 + .05 * distance
    elif postage_type == "package":
        return 2.95 + .25 * distance
    elif postage_type == "large_package":
        return 3.95 + .35 * distance
def main():
    while True:
        run_the_code = str.lower(input("Would you like to run the code? \n"))
        if 'no' in run_the_code:
            print('OK')
            break
        else:
            try:

                dimensions = input("Enter the data as 'Length, Height, Width, Starting Zip Code, Ending Zip Code:  ").split(",")
                length = float(dimensions[0])                               #sets the variable 'lenght' = to the first user input
                height = float(dimensions[1])                               #sets the variable 'height' = to the second user input                                      
                width = float(dimensions[2])                                #sets the variable 'width' = to the third user input
                zip_start = int(dimensions[3])                              #sets the variable 'zip_start' = to the fourth user input
                zip_end = int(dimensions[4])                                #sets the variable 'zip_end' = to the fifth user input
                distance = abs(get_zone(zip_end) - get_zone(zip_start))
                #types_of_packages = ['reg_post_card', 'large_post_card', 'envelope', 'large_envelope', 'package', 'large_package']
                #intial_package_costs = [.20, .37, .37, .60, 2.95, 3.95]
                if length < 0:
                    print('Length cannot be negative.')                     #checks to see if the input 'length' is negative. if it is, the loop will require that the data is re-entered
                elif height < 0:
                    print('Height cannot be negative.')                     #checks to see if the input 'height' is negative. if it is, the loop will require that the data is re-entered 
                elif width < 0:
                    print('Width cannot be negative.')                      #checks to see if the input 'width' is negative. if it is, the loop will require that the data is re-entered
                else:                                                       #if all variables check out (not negative), the code will proceed. 
                    postage_type = get_postage_type(length, height, width)
                    total_cost = calculate_cost(postage_type, distance)
                    print(f'Total Cost = {total_cost:.2f}')
                    user_breakdown_cost = str.lower(input('Would you like me to breakdown the cost formula? '))
                    if 'y' in user_breakdown_cost:
                        #print(f'''Your package is a(n) {postage_type}, and you are shipping it across {distance} shipping zones.
                              #The initial cost for a(n) {postage_type} is {intial_package_costs[]}''')                            
            except ValueError:
                "Please check all of your entries and make sure they correspond with the format."
if __name__ == "__main__":
    main()
