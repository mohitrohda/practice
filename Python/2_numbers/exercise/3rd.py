#You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length. 
#If tiles cost 500 rs per square feet, how much will be the total cost to replace all tiles.
#Calculate and print the cost using python (Hint: Use power operator ** to find area of a square)

length_of_bathroom = 5.5
cost_of_tile = 500

Area_of_bathroom = length_of_bathroom ** 2

total_cost = Area_of_bathroom * cost_of_tile

print("The total cost to replace all tiles is", total_cost)