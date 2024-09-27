Name: toub_julian_PostOffice.py

Description: This code simulates a post office. The user provides the office with 5 inputs: length, width, height,
starting zip code, and the destination zip code. The purpose of the program is to calculate the cost of shipping
the package. The distance shipped is calculated by assigning zone numbers to zip codes that are in certain areas and then 
subtracting the destination's zone by the starting zone. Each package type has a corresponding initial cost and cost per zone. 
The equation: price = initial cost + (cost per zone * distance between zones) is the formula for this program. 
The program also provides a breakdown of the price and allows the user to export to excel. 

Example:
4, 5, .01, 06830, 67840 will return $0.32.

Bugs: none found

Features: breaks down the cost formula, exports to excel 

Sources: https://programming-24.mooc.fi/part-4/5-print-statement-formatting (used on line 164), 
password_keeper.py (by Julian Toub)

Log: 1
