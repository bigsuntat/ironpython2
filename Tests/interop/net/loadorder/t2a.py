# Licensed to the .NET Foundation under one or more agreements.
# The .NET Foundation licenses this file to you under the Apache 2.0 License.
# See the LICENSE file in the project root for more information.

    
from iptest.assert_util import *


add_clr_assemblies("loadorder_2")

# namespace First {
#     public class Nongeneric1 {
#         public static string Flag = typeof(Nongeneric1).FullName;
#     }
# }

import First

add_clr_assemblies("loadorder_2a")

# // non-generic type, which has different namespace, same name from First.Nongeneric1
# namespace Second {
#     public class Nongeneric1 {
#         public static string Flag = typeof(Nongeneric1).FullName;
#     }
# }

import Second

AreEqual(First.Nongeneric1.Flag, "First.Nongeneric1")
AreEqual(Second.Nongeneric1.Flag, "Second.Nongeneric1")

from First import *

AreEqual(Nongeneric1.Flag, "First.Nongeneric1")

from Second import *

AreEqual(Nongeneric1.Flag, "Second.Nongeneric1")

from First import *

AreEqual(Nongeneric1.Flag, "First.Nongeneric1")
