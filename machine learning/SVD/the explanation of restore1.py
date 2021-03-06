import numpy as np


def explanation():
    a=list(range(15))
    am=np.array(a).reshape(5,3)
    print("原始矩阵{}".format(am[:,:]))
    u_r, sigma_r, v_r = np.linalg.svd(am)
    print('矩阵u{}'.format(u_r))
    print('矩阵sigma{}'.format(sigma_r))
    print('矩阵v{}'.format(v_r))
    m = len(u_r)
    n = len(v_r[0])
    a = np.zeros((m, n))
    for k in range(3):
        uk = u_r[:, k].reshape(m, 1)
        vk = v_r[k].reshape(1, n)
        print('----------u{}----------'.format(k))
        print(uk)
        print('---------v{}---------'.format(k))
        print(vk)
        b=sigma_r[k] * np.dot(uk, vk)
        print('u,v.sigma的乘积{}'.format(k,b))
        a += sigma_r[k] * np.dot(uk, vk)
        print('----------------------------------')
        print(a)
        np.set_printoptions(suppress=True)

if __name__ == "__main__":
    explanation()
