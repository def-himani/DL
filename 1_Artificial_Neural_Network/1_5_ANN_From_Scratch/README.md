1_1 and 1_2 performs GD with Numerical Differenciation method.
Other way to calculate GD is through error backpropagation and auto differenciation thats done later in the course i am doing.

1_1 is about SLP - Linear | binary classification | Will observe a linear (line) separation between the binary data
1_2 is about Two layered perceptron - non-linear | binary classification | will observe a curve separating the binary data

1_3 : is about impact of using a linear activation function in hidden layers of a two layer perceptron (non-linear) | binary classification | will observe collapse of 2 layer perceptron network (non-linear) into a linear function due to linear activation function.

Numerical Differentiation:

A method used to approximate the gradient (derivative) of that error with respect to the parameters ($\frac{\partial L}{\partial w}$) using finite differences

central difference: $\frac{L(w+h) - L(w-h)}{2h}$

## (a) Numerical Differentiation (Central Difference Approximation)

$$\frac{\partial L}{\partial w_1} \approx \frac{L(w_1 + h, w_2, \dots, b) - L(w_1 - h, w_2, \dots, b)}{2h}$$

Parameter Matrix & Gradient Matrix$$p[i] = \begin{bmatrix} w_{0,0} & w_{0,1} & \cdots \\ w_{1,0} & w_{1,1} & \cdots \\ \vdots & \vdots & \ddots \end{bmatrix}$$ $$\text{grad} = \begin{bmatrix} \frac{\partial L}{\partial w_{0,0}} & \frac{\partial L}{\partial w_{0,1}} & \cdots \\ \frac{\partial L}{\partial w_{1,0}} & \frac{\partial L}{\partial w_{1,1}} & \cdots \\ \vdots & \vdots & \ddots \end{bmatrix}$$

## (b) Gradient Descent Formula (Parameter Update Rule)

$$w_{t+1} = w_t - \alpha \frac{\partial L(w)}{\partial w}$$
