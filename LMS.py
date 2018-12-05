import numpy as np

def distance(p1,p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def LMS(points, t, n):
    p = int(t + n / 2)
    X = [points[i][0] for i in range(t, t + n)]
    X2 = [X[i] ** 2 for i in range(n)]
    Y = [points[i][1] for i in range(t, t + n)]
    Y2 = [Y[i] ** 2 for i in range(n)]
    XY = [X[i] * Y[i] for i in range(n)]
    X2Y2 = [X[i] ** 2 + Y[i] ** 2 for i in range(n)]
    XX2Y2 = [X[i] * X2Y2[i] for i in range(n)]
    YX2Y2 = [Y[i] * X2Y2[i] for i in range(n)]
    sum_X = sum(X)
    sum_Y = sum(Y)
    sum_XY = sum(XY)
    sum_X2 = sum(X2)
    sum_Y2 = sum(Y2)
    sum_X2Y2 = sum(X2Y2)
    sum_XX2Y2 = sum(XX2Y2)
    sum_YX2Y2 = sum(YX2Y2)
    A = np.array(([sum_X2, sum_XY, sum_X],
                  [sum_XY, sum_Y2, sum_Y],
                  [sum_X, sum_Y, n]))
    B = np.array(([-sum_XX2Y2, -sum_YX2Y2, -sum_X2Y2]))
    try:
        a, b, c = np.matmul(np.linalg.inv(A), B)
        if (a ** 2 + b ** 2) / 4 - c > 0:
            return p, ((a ** 2 + b ** 2) / 4 - c) ** 0.5, -a / 2, -b / 2

        else:
            beta1 = 0.9
            beta2 = 0.999
            e = 1e-8
            step = 0.01
            a = b = c = 0
            v = np.array(([a, b, c]))
            m = s = np.array(([0, 0, 0]))
            Der_a = Der_b = Der_c = 100
            count = 0
            while (count < 100000):
                count += 1
                # print(Der_a,Der_b,Der_c)
                Der_a = (a * sum_X2 + b * sum_XY + c * sum_X + sum_XX2Y2) / 100000
                Der_b = (a * sum_XY + b * sum_Y2 + c * sum_Y + sum_YX2Y2) / 100000
                Der_c = (a * sum_X + b * sum_Y + c * n + sum_X2Y2) / 100000
                V = np.array(([Der_a, Der_b, Der_c]))
                '''m=beta1*m+(1-beta1)*V
                m=m/(1-beta1)
                s=beta2*s+(1-beta2)*np.array(([Der_a**2,Der_b**2,Der_c**2]))
                s=s/(1-beta2)
                print(m,s)
                v=v+step*np.array(([m[0]/(s[0]+e)**0.5,m[1]/(s[1]+e)**0.5,m[2]/(s[2]+e)**0.5]))'''
                a, b, c = np.array(([a, b, c])) - step / count ** 0.5 * V
            if (a ** 2 + b ** 2) / 4 - c > 0:
                return p, ((a ** 2 + b ** 2) / 4 - c) ** 0.5, -a / 2, -b / 2
            else:
                while ((a ** 2 + b ** 2) / 4 - c < 0):
                    count += 1
                    # print(Der_a, Der_b, Der_c)
                    Der_a = (a * sum_X2 + b * sum_XY + c * sum_X + sum_XX2Y2) / 100000
                    Der_b = (a * sum_XY + b * sum_Y2 + c * sum_Y + sum_YX2Y2) / 100000
                    Der_c = (a * sum_X + b * sum_Y + c * n + sum_X2Y2) / 100000
                    V = np.array(([Der_a, Der_b, Der_c]))
                    '''m=beta1*m+(1-beta1)*V
                    m=m/(1-beta1)
                    s=beta2*s+(1-beta2)*np.array(([Der_a**2,Der_b**2,Der_c**2]))
                    s=s/(1-beta2)
                    print(m,s)
                    v=v+step*np.array(([m[0]/(s[0]+e)**0.5,m[1]/(s[1]+e)**0.5,m[2]/(s[2]+e)**0.5]))'''
                    a, b, c = np.array(([a, b, c])) - step / count ** 0.5 * V
                return p, ((a ** 2 + b ** 2) / 4 - c) ** 0.5, -a / 2, -b / 2
    except:
        beta1 = 0.9
        beta2 = 0.999
        e = 1e-8
        step = 0.01
        a = b = c = 0
        v = np.array(([a, b, c]))
        m = s = np.array(([0, 0, 0]))
        Der_a = Der_b = Der_c = 100
        count = 0
        while (count < 100000):
            count += 1
            # print(Der_a, Der_b, Der_c)
            Der_a = (a * sum_X2 + b * sum_XY + c * sum_X + sum_XX2Y2) / 100000
            Der_b = (a * sum_XY + b * sum_Y2 + c * sum_Y + sum_YX2Y2) / 100000
            Der_c = (a * sum_X + b * sum_Y + c * n + sum_X2Y2) / 100000
            V = np.array(([Der_a, Der_b, Der_c]))
            '''m=beta1*m+(1-beta1)*V
            m=m/(1-beta1)
            s=beta2*s+(1-beta2)*np.array(([Der_a**2,Der_b**2,Der_c**2]))
            s=s/(1-beta2)
            print(m,s)
            v=v+step*np.array(([m[0]/(s[0]+e)**0.5,m[1]/(s[1]+e)**0.5,m[2]/(s[2]+e)**0.5]))'''
            a, b, c = np.array(([a, b, c])) - step / count ** 0.5 * V
        if (a ** 2 + b ** 2) / 4 - c > 0:
            return p, ((a ** 2 + b ** 2) / 4 - c) ** 0.5, -a / 2, -b / 2
        else:
            while ((a ** 2 + b ** 2) / 4 - c < 0):
                count += 1
                # print(Der_a, Der_b, Der_c)
                Der_a = (a * sum_X2 + b * sum_XY + c * sum_X + sum_XX2Y2) / 100000
                Der_b = (a * sum_XY + b * sum_Y2 + c * sum_Y + sum_YX2Y2) / 100000
                Der_c = (a * sum_X + b * sum_Y + c * n + sum_X2Y2) / 100000
                V = np.array(([Der_a, Der_b, Der_c]))
                '''m=beta1*m+(1-beta1)*V
                m=m/(1-beta1)
                s=beta2*s+(1-beta2)*np.array(([Der_a**2,Der_b**2,Der_c**2]))
                s=s/(1-beta2)
                print(m,s)
                v=v+step*np.array(([m[0]/(s[0]+e)**0.5,m[1]/(s[1]+e)**0.5,m[2]/(s[2]+e)**0.5]))'''
                a, b, c = np.array(([a, b, c])) - step / count ** 0.5 * V
            return p, ((a ** 2 + b ** 2) / 4 - c) ** 0.5, -a / 2, -b / 2

