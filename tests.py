import unittest

from safe_code_eval import SafeCodeEval, _execute


class TestSafeCodeEval(unittest.TestCase):

    def test_info(self):
        inst = SafeCodeEval()
        _ = inst._info

    def test_compute(self):
        inst = SafeCodeEval()
        test_cases = ["assert add(2, 3) == 5"]
        candidates = [["def add(a,b): return a*b", "def add(a, b): return a+b"]]
        pass_at_k, results = inst.compute(
            references=test_cases,
            predictions=candidates,
            k=[1, 2],
        )
        pass_at_k == {"pass@1": 0.5, "pass@2": 1.0}

        pass_at_k, results = inst.compute(
            references=test_cases,
            predictions=candidates,
            k=[1, 2],
            timeout=0,
        )
        pass_at_k == {"pass@1": 0.0, "pass@2": 0.0}

    def test_execute(self):
        code = "1 + 1"
        result = _execute(code, timeout=5.0)
        self.assertTrue(result["passed"])
        self.assertEqual(result["result"], "")
        self.assertEqual(result["stdout"], "2")
        self.assertEqual(result["stderr"], "")

        code = "1 / 0"
        result = _execute(code, timeout=5.0)
        self.assertFalse(result["passed"])
        self.assertIn("ZeroDivisionError", result["result"])
        self.assertEqual(result["stdout"], "")
        self.assertIn("ZeroDivisionError", result["stderr"])

        code = "import nonexistent"
        result = _execute(code, timeout=5.0)
        self.assertFalse(result["passed"])
        self.assertIn("ModuleNotFoundError", result["result"])
        self.assertEqual(result["stdout"], "")
        self.assertIn("ModuleNotFoundError", result["stderr"])

        code = "assert False"
        result = _execute(code, timeout=5.0)
        self.assertFalse(result["passed"])
        self.assertIn("AssertionError", result["result"])
        self.assertEqual(result["stdout"], "")
        self.assertIn("AssertionError", result["stderr"])
