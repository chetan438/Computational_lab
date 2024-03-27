#question 1
n= input("Enter number of elements")
for i=0:n
  printf("Enter elements into x[n]")
  x(i) = input("x[")
end

for i=0:n
  printf("Enter elements into y[n]")
  x(i) = input("x[")
end
t=o:0:x(n-1)
for i=0:n
  for k=0:n
    z(k) = x(i)*y(n+k)
  endfor
end
plot(z,t)
