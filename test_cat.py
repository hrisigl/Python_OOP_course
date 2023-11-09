class Cat:
    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


from unittest import TestCase, main


class CatTests(TestCase):
    def setUp(self) -> None:
        self.cat = Cat("Mac")

    def test_init(self):
        self.assertEqual("Mac", self.cat.name)
        self.assertEqual(False, self.cat.fed)
        self.assertEqual(False, self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_eat_fed_true_raises(self):
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual('Already fed.', str(ex.exception))

    def test_eat_fed_false_sets_fed_and_sleepy_true(self):
        self.cat.fed = False
        self.assertEqual(False, self.cat.fed)

        self.cat.eat()

        self.assertEqual(True, self.cat.fed)
        self.assertEqual(True, self.cat.sleepy)

    def test_eat_fed_false_size_increases(self):
        self.cat.fed = False
        self.cat.size = 0
        self.assertEqual(0, self.cat.size)

        self.cat.eat()
        self.assertEqual(1, self.cat.size)

        self.cat.fed = False
        self.cat.eat()
        self.assertEqual(2, self.cat.size)

    def test_sleep_if_fed_false_raises(self):
        self.cat.fed = False
        self.assertEqual(False, self.cat.fed)

        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_sleep_if_fed_true_sets_sleepy_to_false(self):
        self.cat.eat()
        self.assertEqual(True, self.cat.fed)
        self.assertEqual(True, self.cat.sleepy)

        self.cat.sleep()
        self.assertEqual(False, self.cat.sleepy)


if __name__ == "__main__":
    main()
