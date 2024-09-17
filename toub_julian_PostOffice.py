'''
Name: 
Description:
Bugs: For example "Fails under x parameters"
Features: 
Sources: 
Log: 1
'''
while True:
    run_the_code = str.lower(input("Would you like to run the code? \n"))
    if 'no' in run_the_code:
        break
    else:
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
                postage_type = 'reg_post_card'
            elif 4.25 < length < 6 and 6 < height < 11 and .007 <= width <= .015:
                postage_type = 'large_post_card'
            elif 3.5 <= length <= 6.125 and 5 <= height <= 11.5 and .016 < width < .25:
                postage_type = 'envelope'
            elif 6.125 < length < 24 and 11 <= height <= 18 and .25 <= width <= .5:
                postage_type = 'large_envelope'
            elif length >= 24 and width >.5 and length + (height*2) + (width*2) <= 84:
                postage_type = 'package'
            elif 84 < length + (length*2) + (width*2) < 130:
                postage_type = 'large_package'
            
            else:
                postage_type = 'unmailable'
                print('This package is unmailable')
            return(postage_type)
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
        def calculate_cost(zip_start, zip_end, postage_type):
            distance = abs(get_zone(zip_end) - get_zone(zip_start))
            
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
                data = input("Enter the data as 'Length, Height, Width, Starting Zip Code, Ending Zip Code:  ")
                dimensions = data.split(',')                                #splits the data inputted by the user into length, height, and width, based on index
                length = float(dimensions[0])                               #sets the variable 'lenght' = to the first user input
                height = float(dimensions[1])                               #sets the variable 'height' = to the second user input                                      
                width = float(dimensions[2])                                #sets the variable 'width' = to the third user input
                zip_start = int(dimensions[3])                              #sets the variable 'zip_start' = to the fourth user input
                zip_end = int(dimensions[4])                                #sets the variable 'zip_end' = to the fifth user input

                if length < 0:
                    print('Length cannot be negative.')                     #checks to see if the input 'length' is negative. if it is, the loop will require that the data is re-entered
                elif height < 0:
                    print('Height cannot be negative.')                     #checks to see if the input 'height' is negative. if it is, the loop will require that the data is re-entered 
                elif width < 0:
                    print('Width cannot be negative.')                      #checks to see if the input 'width' is negative. if it is, the loop will require that the data is re-entered
                else:                                                       #if all variables check out (not negative), the code will proceed. 
                    break

            postage_type = get_postage_type(length, height, width)
            #print(f'Your shipment is a {postage_type}. ')
            #print(f'''{distance = abs(get_zone(zip_end) - get_zone(zip_start))}, {postage_type}''')
                
            print(f'Total Cost = {calculate_cost(zip_start, zip_end, postage_type)}')
            print(length, height, width, zip_start, zip_end)
            print(postage_type)
            print (length + (length*2) + (width*2))
        if __name__ == "__main__":
            main()
