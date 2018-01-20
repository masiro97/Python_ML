
def hypothesis(w,b,x):
    h = w*x +b
    return h

def GradientDescent2(Input,Output,theta,alpha,set):
    multi_wx = hypothesis(theta[1],theta[0],Input)
    loss = multi_wx - Output
    if set ==0:
        gradient = sum(loss) / len(Input)
        theta[0] = theta[0] - alpha * gradient
        return theta[0]
    elif set ==1:
        result = loss * Input
        gradient = sum(result) / len(Input)
        theta[1] = theta[1] - alpha*gradient
        return theta[1]

