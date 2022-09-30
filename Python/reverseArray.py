numberOfRuns=int(input("Enter no of times the program will run!!"))
i=1
while i<=numberOfRuns:
  numberOfElements=int(input("Enter the elements in array"))
  arr=[int(x) for x in input().split()]
  start=0
  end=len(arr)-1
  while start<=end:
    arr[start],arr[end]=arr[end],arr[start]
    start=start+1
    end=end-1
  for j in arr:
    print(j,end=" ")
  i=i+1
  print()