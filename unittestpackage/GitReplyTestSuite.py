import unittest
from unittestpackage.CreatingReply import CreateRepl
from unittestpackage.ChangeReply import ChangeRepl
from unittestpackage.DeleteReply import DeleteRepl

# Get all tests from CreatingReply, ChangeReply and DeleteRepl

tc1 = unittest.TestLoader().loadTestsFromTestCase(CreateRepl)
tc2 = unittest.TestLoader().loadTestsFromTestCase(ChangeRepl)
tc3 = unittest.TestLoader().loadTestsFromTestCase(DeleteRepl)
# Create a test suite combining all test cases

smokeTest = unittest.TestSuite([tc1, tc2, tc3])

unittest.TextTestRunner(verbosity=2).run(smokeTest)
