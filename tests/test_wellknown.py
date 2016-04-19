from django.test import TestCase
from wellknown import models


class WellKnownIntegrationTest(TestCase):

    def testFetchAcmeChallenge(self):
        PATH = 'acme-challenge/challenge-request'
        DATA = 'challenge-response'
        models.Resource(
            path=PATH,
            content=DATA).save()
        response = self.client.get(
            '/.well-known/%s' % PATH)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, DATA)
