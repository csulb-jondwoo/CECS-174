#Jon Ham
#CECS 174

print("Enter integers one by one.")
userList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in userList:
	invalid = True
	while invalid:
		userList[i] = input("Enter integer: ")
		if userList[i].isalpha():
			print("Invalid Entry. Try again.")
		else:
			userList = [int(i) for i in userList]
			break
print()

print("MENU OPTIONS:")


invalid_2 = True
while invalid_2:
	print("1.Display Numbers\n"
	  "2.Display Reversed Numbers\n"
	  "3.Compute Sum\n"
	  "4.Compute Average\n"
	  "5.Maximum Value\n"
	  "6.Minimum Value\n"
	  "7.Display Value at Index\n"
	  "8.Find Matching Value\n"
	  "9.Replace Value\n"
	  "10.Frequency\n"
	  "11.Quit")
	print()
	userSelect = input("Enter your selection: ")
	if userSelect.isalpha():
		print("Invalid entry. Please try again.")
	else:
		userSelect = int(userSelect)
		if userSelect == 0 or userSelect > 11:
			print("Invalid entry. Please try again.")
			print()
		elif userSelect == 1:
			count = 0
			for i in userList:
				while count < 5:
					print(userList[count], end=" ")
					count += 1
				print("")
				while count >= 5 and count < 10:
					print(userList[count], end=" ")
					count += 1
			print("")
		elif userSelect == 2:
			for i in range(9, -1, -1):
				print(userList[i], end=" ")
			print("\n")
		elif userSelect == 3:
			total = 0
			for i in range(0, 10):
				total += userList[i]
			print("The total is", total)
			print()
		elif userSelect == 4:
			total = 0
			for i in range(0, 10):
				total += userList[i]
			average = total / 10
			print("The average is", average)
			print()
		elif userSelect == 5:
			max = userList[0]
			for i in range(0, 10):
				if userList[i] > max:
					max = userList[i]
			print("The maximum value is", max)
			print()
		elif userSelect == 6:
			min = userList[0]
			for i in range(0, 10):
				if userList[i] < min:
					min = userList[i]
			print("The minimum value is", min)
			print()
		elif userSelect == 7:
			invalid_index = True
			while invalid_index:
				index = input("Enter index: ")
				if index.isalpha():
					print("Invalid index.")
				else:
					index = int(index)
					if index < 0 or index > 9:
						print("Invalid index. Try again")
					else:
						print("The value at index", index, "is", userList[index])
						break
			print()
		elif userSelect == 8:
			invalid_match = True
			found = False
			while invalid_match:
				valueMatch = input("Enter value: ")
				if valueMatch.isalpha():
					print("Invalid entry. Please try again")
				else:
					valueMatch = int(valueMatch)
					for i in range(0, 10):
						if valueMatch == userList[i]:
							print("Value was found at index", i)
							found = True
					invalid_match = False
					if not(found):
						print("Value is not within the list")
			print()
		elif userSelect == 9:
			invalid_replace_index = True
			invalid_replace_value = True
			while invalid_replace_index:
				index = input("Enter index: ")
				if index.isdigit():
					index = int(index)
					if index < 0 or index > 9:
						print("Invalid index.")
					else:
						invalid_replace_index = False
				else:
					print("invalid entry.")
			while invalid_replace_value:
				newValue = input("Enter value: ")
				if newValue.isalpha():
					print("Invalid entry.")
				else:
					newValue = int(newValue)
					userList[index] = newValue
					invalid_replace_value = False
			print()
		elif userSelect == 10:
			invalid_freq = True
			while invalid_freq:
				userValue = input("Enter a value: ")
				if userValue.isalpha():
					print("Invalid Entry")
				else:
					userValue = int(userValue)
					counter = 0
					for i in range(0, 10):
						if userValue == userList[i]:
							counter += 1
					print("The value appears", counter,"times.")
					break
			print()
		elif userSelect == 11:
			print("Goodbye!")
			break