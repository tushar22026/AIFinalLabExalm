scored1 = (1,2,4,5,1,5,2)
result1 = sum(scored1)
scored2 = (5,5,2,2,5,2,3)
result2 = sum(scored2)

if result1>result2:
    print("First team won the series.")

elif result1<result2:
    print("First team lost the series.")

else:
    print("First and Second team are equal.")
