import math
x = list(map(int, input().split(',')))  #input vaue of X
y = list(map(int, input().split(',')))  #input vaue of y    

sum_x=0
sum_y=0
for ik in range(len(x)):
    sum_x+=x[ik]
    sum_y+=y[ik]

xy=[]
for i in range(len(x)):
    xy.append(x[i]*y[i])

x_square=[]
for j in x:
    x_square.append(j*j)

y_square=[]
for k in y:
    y_square.append(k*k)

x_bar=sum_x/len(x)

y_bar=sum_y/len(y)

correlation_coffecient=(sum(xy)-(len(x)*x_bar*y_bar))/math.sqrt((sum(x_square)-(len(x)*x_bar*x_bar))*(sum(y_square)-(len(x)*y_bar*y_bar)))

for i in range(len(x)):
    print('|',x[i],'|',y[i],'|',xy[i],'|',x_square[i],'|',y_square[i],'|')
    
print('SUM=|',sum_x,'|',sum_y,'|',sum(xy),'|',sum(x_square),'|',sum(y_square),'|')
print(sum_x,sum_y)
print(xy)
print('x^2 ',x_square)
print('y^2 ',y_square)
print('x_bar:',x_bar,'Y_bar:',y_bar)
print('correlation coffecient, r : {:.2f}'.format(correlation_coffecient))

# regression
print('regression:')
betta=(sum(xy)-(len(x)*x_bar*y_bar))/(sum(x_square)-(len(x)*x_bar*x_bar))
print('Betta {:.3f}'.format(betta))
abc=float('{:.3f}'.format(betta))
alpha=y_bar-(abc*x_bar)
print('Alpha {:.3f}'.format(alpha))
