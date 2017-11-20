from hamcrest import *
import unittest

from django.test import Client

class StudentTest(unittest.TestCase):
    def testBasic(self):
        a = "A"
        b = "A"
        assert_that(a,equal_to(b))


    def testWithoutLog(self):
        c = Client()
        response = c.get("/test/21/start/")
            #self.assertEqual(response.status_code, 404)
        assert_that(response.status_code,404)


    # We test to access to a test that the professor hasn't activated.
    def testNotRunnnig(self):
        c = Client()
        c.login(username="eleve.eleve",password="eleve")
        response = c.get("/student/test/start/465")
        #self.assertTemplateUsed(response,'examinations/test_closed.haml')
        assert_that(response,'examinations/test_closed.haml')

    #
    def testStarted(self):
        c = Client()
        c.login(username="eleve.eleve",password="eleve")
        response = c.get("/student/test/23")
        #self.assertTemplateUsed(response,"examinations/pass_test.haml")
        assert_that(response,"examinations/pass_test.haml")

    # We test to access to the test page where we've already passed the test.
    def testFinished(self):
        c = Client()
        c.login(username="eleve.eleve",password="eleve")
        response = c.get("/student/test/28")
        #self.assertTemplateUsed(response,"examinations/test_finished.haml")
        assert_that(response,"examinations/test_finished.haml")

    # We test to access to a test that we didn't finished
    def testRender(self):
        c = Client()
        c.login(username="eleve.eleve",password="eleve")
        response = c.get("/student/test/28")
        #self.assertTemplateUsed(response,"examinations/take_exercice.haml")
        assert_that(response,"examinations/take_exercice.haml")


if __name__ == '__main__':

    unittest.main()


