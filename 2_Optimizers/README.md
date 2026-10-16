# 2.1 Optimizer


![alt text](./img/image-10.png)



 ## 1.0. SGD optimizer

 ![alt text](./img/image-0.png)

 ![alt text](./img/image-1.png)


 ## 2.0 Momentum optimizer

 ![alt text](./img/image-2.png)

 ![alt text](./img/image-3.png)


 # observation

- the data is set up in a way that W1 has a has a softer slope, and W2 has a steeper slope.
- on running GD optimizer, the Data oscillates between W1 and W2
- on applying momentum optimizer, the momentum from the previous gradient descent will reduce drastic movement on either direction. Hence the oscillating phenomenon is reduced and helps it to converge to the target faster and reliably.



## 3) Adagrad

![alt text](./img/image-4.png)

![alt text](./img/image-5.png)


## 4) RMSprop


### (i) learning_rate = 0.2, rho=0.9

![alt text](./img/image-6.png)

![alt text](./img/image-7.png)

### (i) learning_rate = 0.2, rho=0.1

![alt text](./img/image-8.png)

![alt text](./img/image-9.png)


## 5) Adadelta