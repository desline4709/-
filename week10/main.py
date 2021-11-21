import numpy as np


class RandomWalk:
    def __init__(self, mu, X_0, sigma2, N):
        self._x_0 = X_0
        self._mu = mu
        self._sigma2 = sigma2
        self._N = N

    @property
    def x_0(self):
        return self._x_0

    @x_0.setter
    def x_0(self, value):
        self._x_0 = value

    @property
    def mu(self):
        return self._mu

    @mu.setter
    def mu(self, value):
        self._mu = value

    @property
    def sigma2(self):
        return self._sigma2

    @sigma2.setter
    def sigma2(self, value):
        self._sigma2 = value

    @property
    def N(self):
        return self._N

    @N.setter
    def N(self, value):
        self._N = value

    def walk(self):
        cot = 0
        x_list = [self._x_0]
        for i in range(self._N):
            if i == 0:
                x = self._x_0
            else:
                sigma = np.sqrt(self._sigma2)
                w_t = np.random.normal(self._mu, sigma, 1)
                x = float(self._mu + x_list[i-1] + w_t)
                x_list.append(x)
            yield x
            cot += 1
        return "现有的序列为{}".format(x_list)

    @property
    def params(self):
        return "参数如下：mu-{}, x_0-{}, sigma^2-{}, N-{}".format(self._mu, self._x_0, self._sigma2, self._N)


class RandomWalks:
    """
    实现多个RandomWalk的合并
    """
    def __init__(self, length):
        self._walk_list = []
        self._length = length

    def add_walk(self, rw: RandomWalk):
        rw.N = self._length  # 长度对齐
        walk = rw.walk()
        self._walk_list.append(walk)

    def walks(self):
        return zip(self._walk_list)





def main():
    '''
    # Test RandomWalk

    test = RandomWalk(0, 0, 1, 5)
    for i in test.walk():
        print(i)
    print(test.params)
    '''
    '''
    # Test RandomWalks
    
    rw1 = RandomWalk(0, 0, 1, 5)
    rw2 = RandomWalk(1, 1, 1, 8)
    rws = RandomWalks(10)
    rws.add_walk(rw1)
    rws.add_walk(rw2)
    walks = list(rws.walks())
    print(walks)
    try:
        while 1:
            res = []
            for walk in walks:
                temp = next(walk[0])
                res.append(temp)
            print(res)
    except StopIteration:
        print('done')
    '''




if __name__ == "__main__":
    main()