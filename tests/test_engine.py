import unittest
from engine.engine import Engine

class TestEngine(unittest.TestCase):

    def test_engine_should_be_serviced(self):
        engine = Engine.needs_service
        self.assertTrue(engine)

if __name__ == '__main__':
    unittest.main()

