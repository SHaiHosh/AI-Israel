import matplotlib.pyplot as plt
# plt.plot(range(10))
# plt.show()

import numpy as np
import pip
installed_packages = pip.get_installed_distributions()
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
     for i in installed_packages])
print(installed_packages_list)

a1=1
import caffe
print a1