from collections import deque


class Lru_Cache(object):
    def __init__(self, size):
        self.size = size
        self.q = deque(maxlen=size)
        self.d = {}

    def set(self, k, v):
        self.d[k] = v
        if len(self.q) == self.size:
            least_recent_key = self.q.popleft()
            self.d.pop(least_recent_key)
        self.q.append(k)

    def get(self, k):
        if k not in self.d:
            return None
        self.q.remove(k)
        self.q.append(k)
        return self.d.get(k)


if __name__ == '__main__':
    c = Lru_Cache(3)
    c.set(1, 'one')
    c.set(2, 'two')
    c.set(3, 'three')
    c.set(4, 'four')
    assert(c.get(1) is None)
    assert(c.get(2) == 'two')
    c.set(1, 'one')
    assert(c.get(3) is None)
