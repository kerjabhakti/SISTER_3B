from __future__ import print_function
import Pyro4

obj = Pyro4.core.Proxy("PYRONAME:example.chainTopology.1")
print("Status = %s" % obj.process(["hello"]))
