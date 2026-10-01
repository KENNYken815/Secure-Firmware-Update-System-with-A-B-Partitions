import unittest
class BootState:
    def __init__(self): self.active='A'; self.pending='A'; self.version=1; self.attempts=0
    def install(self,v):
        if v<self.version:return False
        self.pending='B' if self.active=='A' else 'A';self.version=v;self.attempts=0;return True
    def boot(self):
        if self.pending!=self.active and self.attempts<3:self.attempts+=1;return self.pending
        self.pending=self.active;self.attempts=0;return self.active
    def confirm(self):self.active=self.pending;self.attempts=0
class TestUpdate(unittest.TestCase):
    def test_inactive_slot(self):
        b=BootState();self.assertTrue(b.install(2));self.assertEqual(b.boot(),'B')
    def test_downgrade_rejected(self):
        b=BootState();self.assertFalse(b.install(0))
    def test_confirm(self):
        b=BootState();b.install(2);b.boot();b.confirm();self.assertEqual(b.active,'B')
    def test_rollback(self):
        b=BootState();b.install(2);self.assertEqual(b.boot(),'B');self.assertEqual(b.boot(),'B');self.assertEqual(b.boot(),'B');self.assertEqual(b.boot(),'A')
if __name__=='__main__':unittest.main()
