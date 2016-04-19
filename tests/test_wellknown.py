from django.test import TestCase
from wellknown import models


class WellKnownIntegrationTest(TestCase):

    def testFetchAcmeChallenge(self):
        DATA = 'challenge-response'
        models.Resource(
            path='acme-challenge/challenge-request',
            content=DATA).save()
        response = self.client.get(
            '/.well-known/acme-challenge/challenge-request')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, DATA)
