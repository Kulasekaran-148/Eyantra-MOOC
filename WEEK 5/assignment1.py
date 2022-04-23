
# No other modules apart from 'argparse' need to be imported
# as they aren't required to solve the assignment

# Import required module/s
import argparse


def raise_power_of_N():
	##############	ADD YOUR CODE HERE	##############
	parser = argparse.ArgumentParser(allow_abbrev=False, description='Calculate square and/or cube of N', epilog='Week-5 Assignment-1')
	parser.add_argument("N", type=int, help='input the number')
	parser.add_argument('-c','--cube', action='store_true', help='calculate cube of N as well')
	args=parser.parse_args()
	print("Square of N:",args.N**2)
	if args.cube:
		print("Cube of N:",args.N**3)
	##################################################


if __name__ == "__main__":
	"""Main function, code begins here
	"""
	raise_power_of_N()
