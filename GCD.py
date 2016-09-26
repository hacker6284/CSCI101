def GCD(X, Y):
    if (X>0):
        if (Y>0):
            if (X>Y):
                if (X%Y>0):
                    return GCD(X%Y,Y)
                else: return Y
            else:
                if (Y%X>0):
                    return GCD(Y%X,X)
                else: return X

print GCD(252, 147)
