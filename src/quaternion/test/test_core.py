import unittest
from quaternion.api import BaseQuaternion, Quaternion

class BaseQuaternionTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_repr(self):
        q = BaseQuaternion(1, 0, 0, 0)
        string = '<BaseQuaternion a=1.0, b=0.0, c=0.0, d=0.0>'

        self.assertEqual(
            repr(q),
            string
        )

    def test_init(self):
        try:
            q = BaseQuaternion(1, 0, 0, 0)
        except Exception:
            self.fail("BaseQuaternion supports initialization via components.")

        try:
            q = BaseQuaternion(BaseQuaternion(1, 0, 0, 0))
        except Exception:
            self.fail(
                "BaseQuaternion supports initialization via subclasses " \
                "of IQuaternion"
            )

        try:
            q = BaseQuaternion('apple')
        except Exception:
            pass
        else:
            self.fail(
                'BaseQuaternion __init__ only supports initialization via' \
                'components (a, b, c, d) or objects of type IQuaternion'
            )

    def test_str(self):
        q = BaseQuaternion(1, 0, 0, 0)
        self.assertEqual(str(q), '1.0')

        q = BaseQuaternion(0, 1, 0, 0)
        self.assertEqual(str(q), '1.0i')

        q = BaseQuaternion(0, 0, 1, 0)
        self.assertEqual(str(q), '1.0j')

        q = BaseQuaternion(0, 0, 0, 1)
        self.assertEqual(str(q), '1.0k')

        q = BaseQuaternion(-1, 0, 0, 0)
        self.assertEqual(str(q), '-1.0')

        q = BaseQuaternion(0, -1, 0, 0)
        self.assertEqual(str(q), '-1.0i')

        q = BaseQuaternion(0, 0, -1, 0)
        self.assertEqual(str(q), '-1.0j')

        q = BaseQuaternion(0, 0, 0, -1)
        self.assertEqual(str(q), '-1.0k')

        q = BaseQuaternion(1, 1, 1, 1)
        self.assertEqual(str(q), '1.0 + 1.0i + 1.0j + 1.0k')

        q = BaseQuaternion(-1, -1, -1, -1)
        self.assertEqual(str(q), '-1.0 - 1.0i - 1.0j - 1.0k')


    def test_components(self):
        q = BaseQuaternion(1, 2, 3, 4)

        self.assertEqual(q.a, 1)
        self.assertEqual(q.b, 2)
        self.assertEqual(q.c, 3)
        self.assertEqual(q.d, 4)

    def test_real(self):
        q = BaseQuaternion(1, 0, 0, 0)
        self.assertEqual(q.real, 1)

    def test_imag(self):
        q = BaseQuaternion(0, 1, 1, 1)
        self.assertEqual(q.imag, (1j, 1j, 1j))

    def test_magnitude(self):
        q = BaseQuaternion(1, 0, 0, 0)
        p = BaseQuaternion(1, 1, 1, 1)
        r = BaseQuaternion(1, -1, -1, -1)

        self.assertEqual(q.magnitude, 1)
        self.assertEqual(p.magnitude, 2)
        self.assertEqual(r.magnitude, 2)

    def test_conjugate(self):
        q = BaseQuaternion(1, 1, 1, 1)
        p = q.conjugate

        self.assertEqual(p.a, 1)
        self.assertEqual(p.b, -1)
        self.assertEqual(p.c, -1)
        self.assertEqual(p.d, -1)

    def test_inverse(self):
        q = BaseQuaternion(1, 1, 1, 1)

        try:
            q.inverse
        except NotImplementedError:
            pass
        else:
            self.fail('Should have raised NotImplemented error.')

class QuaternionTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_repr(self):
        q = Quaternion(1, 0, 0, 0)
        string = '<Quaternion a=1.0, b=0.0, c=0.0, d=0.0>'

        self.assertEqual(
            repr(q),
            string
        )

    def test_add(self):
        q = Quaternion(1, 1, 1, 1)
        p = Quaternion(1, 1, 1, 1)

        r = q + p

        self.assertEqual(r.a, 2.0)
        self.assertEqual(r.b, 2.0)
        self.assertEqual(r.c, 2.0)
        self.assertEqual(r.d, 2.0)

        t = p + q

        self.assertEqual(r.a, 2.0)
        self.assertEqual(r.b, 2.0)
        self.assertEqual(r.c, 2.0)
        self.assertEqual(r.d, 2.0)

        p = Quaternion(0, 0, 0, 0)

        s = p + q

        self.assertEqual(s.a, 1)
        self.assertEqual(s.b, 1)
        self.assertEqual(s.d, 1)
        self.assertEqual(s.c, 1)


    def test_iadd(self):
        q  = Quaternion(1, 1, 1, 1)
        q += Quaternion(1, 1, 1, 1)

        self.assertEqual(q.a, 2.0)
        self.assertEqual(q.b, 2.0)
        self.assertEqual(q.c, 2.0)
        self.assertEqual(q.d, 2.0)

        q  = Quaternion(1, 1, 1, 1)
        q += Quaternion(0, 0, 0, 0)

        self.assertEqual(q.a, 1.0)
        self.assertEqual(q.b, 1.0)
        self.assertEqual(q.c, 1.0)
        self.assertEqual(q.d, 1.0)

        q = Quaternion(0, 0, 0, 0)
        q += Quaternion(1, 1, 1, 1)

        self.assertEqual(q.a, 1.0)
        self.assertEqual(q.b, 1.0)
        self.assertEqual(q.c, 1.0)
        self.assertEqual(q.d, 1.0)



    def test_sub(self):
        q = Quaternion(1, 1, 1, 1)
        p = Quaternion(0, 0, 0, 0)

        r = q - p

        self.assertEqual(r.a, 1.0)
        self.assertEqual(r.b, 1.0)
        self.assertEqual(r.c, 1.0)
        self.assertEqual(r.d, 1.0)

        s = p - q

        self.assertEqual(s.a, -1.0)
        self.assertEqual(s.b, -1.0)
        self.assertEqual(s.c, -1.0)
        self.assertEqual(s.d, -1.0)

        p = Quaternion(1, 1, 1, 1)
        t = q - p

        self.assertEqual(t.a, 0)
        self.assertEqual(t.b, 0)
        self.assertEqual(t.c, 0)
        self.assertEqual(t.d, 0)

    def test_isub(self):
        q  = Quaternion(1, 1, 1, 1)
        q -= Quaternion(1, 1, 1, 1)

        self.assertEqual(q.a, 0.0)
        self.assertEqual(q.b, 0.0)
        self.assertEqual(q.c, 0.0)
        self.assertEqual(q.d, 0.0)

        q = Quaternion(0, 0, 0, 0)
        q -= Quaternion(1, 1, 1, 1)

        self.assertEqual(q.a, -1.0)
        self.assertEqual(q.b, -1.0)
        self.assertEqual(q.c, -1.0)
        self.assertEqual(q.d, -1.0)

        q = Quaternion(1, 1, 1, 1)
        q -= Quaternion(0, 0, 0, 0)

        self.assertEqual(q.a, 1.0)
        self.assertEqual(q.b, 1.0)
        self.assertEqual(q.c, 1.0)
        self.assertEqual(q.d, 1.0)

    def test_mul_by_scalar(self):
        q = Quaternion(0.5, 0.5, 0.5, 0.5)

        p = q * 2
        r = 2 * q

        self.assertTrue(p.a, 1)
        self.assertTrue(p.b, 1)
        self.assertTrue(p.c, 1)
        self.assertTrue(p.d, 1)

        self.assertTrue(r.a, 1)
        self.assertTrue(r.b, 1)
        self.assertTrue(r.c, 1)
        self.assertTrue(r.d, 1)

        p = q * 1
        r = 1 * q

        self.assertTrue(p.a, 0.5)
        self.assertTrue(p.b, 0.5)
        self.assertTrue(p.c, 0.5)
        self.assertTrue(p.d, 0.5)

        self.assertTrue(r.a, 0.5)
        self.assertTrue(r.b, 0.5)
        self.assertTrue(r.c, 0.5)
        self.assertTrue(r.d, 0.5)

    def test_neg(self):
        q = Quaternion(1, 1, 1, 1)

        p = -q

        self.assertTrue(p.a, -1)
        self.assertTrue(p.b, -1)
        self.assertTrue(p.c, -1)
        self.assertTrue(p.d, -1)

        r = -p

        self.assertTrue(r.a, 1)
        self.assertTrue(r.b, 1)
        self.assertTrue(r.c, 1)
        self.assertTrue(r.d, 1)

    def test_div_by_scalar(self):
        q = Quaternion(1, 1, 1, 1)

        p = q / 2

        self.assertTrue(p.a, 0.5)
        self.assertTrue(p.b, 0.5)
        self.assertTrue(p.c, 0.5)
        self.assertTrue(p.d, 0.5)

        #equivalent to 2 * q.inverse
        r = 2 / q

        self.assertTrue(r.a,  0.5)
        self.assertTrue(r.b, -0.5)
        self.assertTrue(r.c, -0.5)
        self.assertTrue(r.d, -0.5)

        p = q / 1

        self.assertTrue(p.a, 1)
        self.assertTrue(p.b, 1)
        self.assertTrue(p.c, 1)
        self.assertTrue(p.d, 1)


    def test_mul_by_quaternion(self):
        q = Quaternion(1, 1, 1, 1)
        p = Quaternion(0.25, -0.25, -0.25, -0.25)

        r = q * p
        t = p * q

        self.assertEqual(r.a, 1)
        self.assertEqual(r.b, 0)
        self.assertEqual(r.c, 0)
        self.assertEqual(r.d, 0)

        self.assertEqual(t.a, 1)
        self.assertEqual(t.b, 0)
        self.assertEqual(t.c, 0)
        self.assertEqual(t.d, 0)

        q = Quaternion(1, 2, 3, 4)
        p = Quaternion(5, 6, 7 ,8)
        r = q * p

        self.assertEqual(r.a, -60)
        self.assertEqual(r.b, 12)
        self.assertEqual(r.c, 30)
        self.assertEqual(r.d, 24)

        s = p * q

        self.assertEqual(s.a, -60)
        self.assertEqual(s.b, 20)
        self.assertEqual(s.c, 14)
        self.assertEqual(s.d, 32)

    def test_imul_by_quaternion(self):
        q = Quaternion(1, 1, 1, 1)
        q *= Quaternion(0.25, -0.25, -0.25, -0.25)

        p = Quaternion(0.25, 0.25, 0.25, 0.25)
        p *=  Quaternion(1, -1, -1, -1)

        self.assertEqual(q.a, 1)
        self.assertEqual(q.b, 0)
        self.assertEqual(q.c, 0)
        self.assertEqual(q.d, 0)

        self.assertEqual(p.a, 1)
        self.assertEqual(p.b, 0)
        self.assertEqual(p.c, 0)
        self.assertEqual(p.d, 0)

        q = Quaternion(1, 2, 3, 4)
        q *= Quaternion(5, 6, 7 ,8)

        self.assertEqual(q.a, -60)
        self.assertEqual(q.b, 12)
        self.assertEqual(q.c, 30)
        self.assertEqual(q.d, 24)

        q = Quaternion(5, 6, 7 ,8)
        q *= Quaternion(1, 2, 3, 4)

        self.assertEqual(q.a, -60)
        self.assertEqual(q.b, 20)
        self.assertEqual(q.c, 14)
        self.assertEqual(q.d, 32)



    def test_div_by_quaternion(self):
        q = Quaternion(1, 1, 1, 1)
        p = Quaternion(1, 1, 1, 1)

        r = q / p
        t = p / q

        self.assertEqual(r.a, 1)
        self.assertEqual(r.b, 0)
        self.assertEqual(r.c, 0)
        self.assertEqual(r.d, 0)

        self.assertEqual(t.a, 1)
        self.assertEqual(t.b, 0)
        self.assertEqual(t.c, 0)
        self.assertEqual(t.d, 0)

        q = Quaternion(1, 2, 3, 4)
        p = Quaternion(5, 6, 7, 8)
        r = q / p

        self.assertAlmostEqual(r.a, 35.0 / 87.0)
        self.assertAlmostEqual(r.b, 4.0 / 87.0)
        self.assertAlmostEqual(r.c, 0.0 / 87.0)
        self.assertAlmostEqual(r.d, 8.0 / 87.0)

        r = p / q

        self.assertAlmostEqual(r.a, 35.0 / 15.0)
        self.assertAlmostEqual(r.b, -4.0 / 15.0)
        self.assertAlmostEqual(r.c,  0.0 / 15.0)
        self.assertAlmostEqual(r.d, -8.0 / 15.0)


    def test_idiv_by_quaternion(self):
        q = Quaternion(1, 1, 1, 1)
        q /= Quaternion(1, 1, 1, 1)

        p = Quaternion(0.25, 0.25, 0.25, 0.25)
        p /=  Quaternion(0.25, 0.25, 0.25, 0.25)

        self.assertEqual(q.a, 1)
        self.assertEqual(q.b, 0)
        self.assertEqual(q.c, 0)
        self.assertEqual(q.d, 0)

        self.assertEqual(p.a, 1)
        self.assertEqual(p.b, 0)
        self.assertEqual(p.c, 0)
        self.assertEqual(p.d, 0)

        q = Quaternion(1, 2, 3, 4)
        q /= Quaternion(5, 6, 7, 8)

        self.assertAlmostEqual(q.a, 35.0 / 87.0)
        self.assertAlmostEqual(q.b, 4.0 / 87.0)
        self.assertAlmostEqual(q.c, 0.0 / 87.0)
        self.assertAlmostEqual(q.d, 8.0 / 87.0)

        q = Quaternion(5, 6, 7, 8)
        q /= Quaternion(1, 2, 3, 4)

        self.assertAlmostEqual(q.a, 35.0 / 15.0)
        self.assertAlmostEqual(q.b, -4.0 / 15.0)
        self.assertAlmostEqual(q.c,  0.0 / 15.0)
        self.assertAlmostEqual(q.d, -8.0 / 15.0)

    def test_inverse(self):
        q = Quaternion(1, 2, 3, 4)
        p = q.inverse

        self.assertAlmostEqual(p.a,  1.0 / 30.0)
        self.assertAlmostEqual(p.b, -2.0 / 30.0)
        self.assertAlmostEqual(p.c, -3.0 / 30.0)
        self.assertAlmostEqual(p.d, -4.0 / 30.0)

        q = Quaternion(1, 1, 1, 1)
        p = q.inverse

        self.assertEqual(p.a, 0.25)
        self.assertEqual(p.b, -0.25)
        self.assertEqual(p.c, -0.25)
        self.assertEqual(p.d, -0.25)

        q = Quaternion(1, 0, 0, 0)
        p = q.inverse

        self.assertEqual(p.a, 1)
        self.assertEqual(p.b, 0)
        self.assertEqual(p.c, 0)
        self.assertEqual(p.d, 0)

        q = Quaternion(1, 1, 1, 1)
        p = q * q.inverse

        self.assertEqual(p.a, 1)
        self.assertEqual(p.b, 0)
        self.assertEqual(p.c, 0)
        self.assertEqual(p.d, 0)

        p = q.inverse * q

        self.assertEqual(p.a, 1)
        self.assertEqual(p.b, 0)
        self.assertEqual(p.c, 0)
        self.assertEqual(p.d, 0)

if __name__ == "__main__":
    unittest.main()
