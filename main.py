import pandas

file = pandas.read_csv("SupermarketCompare.csv")

# Finding the average cost of each item
average_costArray = []


def calculateAverage(rowPosition, item):
    array_name = item + "_Average"
    array_name = []
    for i in range(1, 4):
        product = file.iloc[rowPosition][i]
        array_name.append(product)

    sum = 0
    average_cost = 0
    for numbers in array_name:
        sum += numbers

    average_cost = sum / 3
    print("Average Cost in",item +":",average_cost)

    average_costArray.append(average_cost)


calculateAverage(0, "bread")
calculateAverage(1, "sugar")
calculateAverage(2, "rice")
calculateAverage(3, "flour")
calculateAverage(4, "coke")

file["Average_Cost"] = average_costArray

file.to_csv("SupermarketCompare.csv", index=False)

# getting the total sales of each supermarket
total_sales = ["Total Sales:"]

print("\n")
def calculateTotal(columnPosition, supermarket):
    array_name = supermarket + "_array"
    array_name = []
    for i in range(5):
        product = file.iloc[i][columnPosition]
        array_name.append(product)

    sum = 0
    for numbers in array_name:
        sum += numbers

    print("Total Spent in",supermarket+":", sum)

    total_sales.append(sum)
    return sum


calculateTotal(1, "Shoprite")
calculateTotal(2, "HMedix")
calculateTotal(3, "Next")

total_sales.append("")

file.loc[len(file)] = total_sales
file.to_csv("SupermarketCompare.csv", index=False)
print(file)
