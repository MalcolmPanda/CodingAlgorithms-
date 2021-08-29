#Brute force method of checking if sum of two numbers of two different arrays add up to a target value
def twoSumBrute(a,b,target):
        # set our found flag to false initally 
        found = False
        for i in range(len(a)):
            print("currnet  i " + str(a[i]))
            # for each value of array a we will print the current value of each index in variable i
            for j in range(len(b)):
                # check each value of i against each value of j with nested loop
                print("current j " + str(b[j]))
                # for each value of array b we will print the current value of j
                if a[i] + b[j] == target:
                    # if our current i value of array a AND j value of array b add up to our target value we print them 
                    # and set our found flag to True and break the second inner loop
                    found = True
                    print("we found it target: "+str(target)+"\n" +str(a[i]) +" and " +str(b[j]))
                    break
                elif not found:
                    # check to see if the found flag is False if its false that means we havent found our target
                    # print the current I and current J we have tried
                    print("Target not found numbers tried: " +str(a[i]) +" and " +str(b[j]))
            if found:
                # check if our found flag is True if it is break out of the First outter loop and end the function
                break
                                
a = [1,2,3,7,9,9]
b = [1,4,2,3,11]
target = 20
twoSumBrute(a,b,target)
