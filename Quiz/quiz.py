print("Welcome to electric bill calculator, developped by Mehmet Soner Korucu!")
while(1):
	try:
		first_name = str(input("Enter your first name: "))
		last_name = str(input("Enter your last name: "))
		eletric_useage = float(input("Enter your electric usage in kilowatt-hours(kWh): "))
		break
	except ValueError:
		print("please enter valid electric usage or name.")

while(1):
	input_discount = input("do you have discount? yes or no: ")
	if (input_discount == "yes" or input_discount == "no"):
		break
	print("please enter a valid input!")
AU = 0.91555
VAT = 0.18
DU = 0.2651
A = AU * eletric_useage
D = DU * eletric_useage
F = 0.007 * A
total_before_VAT = A + F
if (input_discount == "no"):
	total_before_VAT += D
total_electric_bill = (1 + VAT) * total_before_VAT
print("Total electric usage with taxes is", round(total_electric_bill))
