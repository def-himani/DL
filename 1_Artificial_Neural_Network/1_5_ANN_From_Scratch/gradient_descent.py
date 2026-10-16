import numpy as np
h = 1e-4
def numerical_differentiation(x, y, f_loss, f_predict, parameters):
    p = parameters
    p_gradients = []
    for i in range(len(p)):
        # ex) p[0]= wh, p[1]= bh,
        #     p[2]= wo, p[3]= bo
        rows, cols = p[i].shape
        grad = np.zeros_like(p[i])
        
        # Apply numerical differentiation to all elements in p[i].
        for row in range(rows):
            for col in range(cols):
                # Measures the change in loss when the p[i][row, col]
                # element changes by h. The remaining elements are
                # fixed. This is an approximate gradient.
                p_org = p[i][row, col]    # original value of p
                p[i][row, col] = p_org + h # The element at position
                                           # (row, col) increases by h.
                y_hat = f_predict(x)       # calculate y_hat
                f1 = f_loss(y, y_hat)      # The amount of change in loss
                
                p[i][row, col] = p_org - h # decreases by h.
                y_hat = f_predict(x)       # calculate y_hat
                f2 = f_loss(y, y_hat)      # The amount of
                                           # change in loss.
                p[i][row, col] = p_org     # Restore p back to
                                           # its original value.
                                           
                # the gradient at position (row, col)
                grad[row, col] = (f1 - f2) / (2. * h)
        p_gradients.append(grad) # gradients for all parameters
    return p_gradients

# Perform Gradient Descent
def gradient_descent(x, y, alpha, f_loss,
                     f_predict, parameters):
    p = parameters
    grad = numerical_differentiation(x, y,
                                     f_loss,
                                     f_predict,
                                     parameters)
                                     
    for i in range(len(p)):
        p[i] = p[i] - alpha * grad[i]