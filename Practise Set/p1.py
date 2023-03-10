class C2dVec:
    def __init__(self,i,j):
        self.icap = i
        self.jcap = j

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"
    
class C3dvec(C2dVec):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.kcap = k

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"
    

v2d = C2dVec(2,3)
v3d = C3dvec(2,3,4)
print(v2d)
print(v3d)
