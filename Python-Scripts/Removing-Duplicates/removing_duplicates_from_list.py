# initializing list
test_list = [12013,
12260,
12262,
12264,
12453,
12327,
11473,
12254,
12281,
12470,
12546,
12292,
12341,
12509,
12602,
12603,
12791,
12931,
12995,
13004,
13050,
13076,
12263,
11957,
12720,
13081,
11935,
12392,
12791,
12509,
12292,
13076,
12936,
13004,
13050,
12602,
12603,
12995,
12459,
12791,
12509,
12292,
13076,
12936,
13004,
13050,
12602,
12603,
12995,
13081,
12012,
12459,
13020,
12298,
12189,
12988,
12304,
12305,
12402]

print ("The original list is : "
		+ str(test_list))

# using set() to remove duplicated from list
test_list = list(set(test_list))

# printing list after removal
# distorted ordering
print ("\nThe list after removing duplicates : "
		+ str(test_list))



