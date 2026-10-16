# 2.1 momentum optimizer

- manually simulated oscillating gradient decent
- perform gradient decent two ways
    - first plain stochastic gradient decent SGD with momentum set to 0
    - change optimizer to SGD with momentum set to 0.2

 ## 1.0. SGD optimizer

 ![alt text](./img/image.png)

 ![alt text](./img/image-1.png)


 ## 2.0 Momentum optimizer

 ![alt text](./img/image-2.png)

 ![alt text](./img/image-3.png)


 # observation

- the data is set up in a way that W1 has a has a softer slope, and W2 has a steeper slope.
- on running GD optimizer, the Data oscillates between W1 and W2
- on applying momentum optimizer, the momentum from the previous gradient descent will reduce drastic movement on either direction. Hence the oscillating phenomenon is reduced and helps it to converge to the target faster and reliably.