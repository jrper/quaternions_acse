import quaternions_acse as q

def q_comp(x,a,b,c,d):
    assert(x.real==a)
    assert(x.imag==b)
    assert(x.imag2==c)
    assert(x.imag3==d)

def test_quaternions_init():
    q_comp(q.Quaternion(), 0, 0, 0, 0)
    q_comp(q.Quaternion(1), 1, 0, 0, 0)
    q_comp(q.Quaternion(1+1j), 1, 1, 0, 0)
    q_comp(q.Quaternion(1, 1, 1, 1), 1, 1, 1, 1)

def test_quaternions_addition():
    q_comp(1.0+q.Quaternion(1), 2.0, 0, 0, 0)
    q_comp(q.Quaternion(1)+q.Quaternion(1), 2, 0, 0, 0)
    z = 1+1j
    q_comp(q.Quaternion(1)+z, 2, 1, 0, 0)
    q_comp(q.Quaternion(1, 2, 3, 4)+q.Quaternion(0, 1, 2 ,3), 1, 3, 5, 7)
    q_comp(q.i+q.j-q.k, 0, 1, 1, -1)
