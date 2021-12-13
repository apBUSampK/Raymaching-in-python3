import vector
import numpy as np


class Sphere:
    def __init__(self, pos: vector.VectorObject3D, r, scale=1, delete=False, luminosity=None):
        self.pos = pos
        self.r = r
        self.scale = scale
        self.delete = delete
        self.luminosity = luminosity

    def dist(self, point: vector.VectorObject3D):
        return self.scale * (abs(self.pos - point) - self.r)

class Parallelepiped:
    def __init__(self, pos: vector.VectorObject3D, a: vector.VectorObject3D, b: vector.VectorObject3D, c: vector.VectorObject3D, scale = 1, delete = False, luminosity = None):
        self.pos = pos
        self.a = a
        self.b = b
        self.c = c
        self.scale = scale
        self.delete = delete
        self.luminosity = luminosity
        
    def dist(self, point: vector.VectorObject3D):
        q = abs(point) - self.pos
        return self.scale * length(max(q,0.0)) + min(max(q.x,max(q.y,q.z)),0.0);

class Plane:
    def __init__(self, n: vector.VectorObject3D, z, delete=False, luminosity=None):
        self.n = n
        self.z = z
        self.delete = delete
        self.luminosity = luminosity

    def dist(self, point: vector.VectorObject3D):
        return point.dot(self.n)/abs(self.n) + self.z
    
    class Torus: 
    def __init__(self, pos: vector.VectorObject3D, t: vector.VectorObject2D, scale = 1, delete = False, luminosity = None):
        self.pos = pos
        self.t = t 
        self.scale = scale
        self.delete = delete
        self.luminosity = luminosity
        
    def dist(self, point: vector.VectorObject3D):
        s = vector.obj(x =  (point - self.pos).x, y = (point - self.pos).y, z = (point - self.pos).z ) 
        w = vector.obj(x =  s.x, y = 0, z = s.z )
        q = vector.obj(x = abs(w) - t.x, y = s.y )
        return self.scale * (abs(q) - t.y)
