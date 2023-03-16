# Vector Module
This Python module provides classes for 2D and 3D vectors, as well as common vector operations.

# Usage
To use this module, simply import it into your Python script:


# Creating Vectors
## To create a new vector, simply instantiate the Vector or ThDVector class with the desired x, y, and z coordinates:

```
v1 = vector.Vector(1, 2)
v2 = vector.ThDVector(1, 2, 3)
```

# Vector Operations
## The following vector operations are supported:

## Scalar Multiplication
### You can multiply a vector by a scalar using the * operator:

```
v3 = v1 * 3
```

## Dot Product
### You can calculate the dot product of two vectors using the funcs.dotproduct() or funcs.thddotproduct() method:

```
vector.funcs.dotproduct(v1, v2)
vector.funcs.thddotproduct(v2, v3)
```

## Cross Product
### You can calculate the cross product of two 3D vectors using the ThDVector.cross() method:

```
v4 = vector.ThDVector(2, 3, 4)
v5 = v2.cross(v4)
```

## Magnitude
### You can calculate the magnitude of a vector using the Vector.magnitude() or ThDVector.magnitude() method:

```
m1 = v1.magnitude()
m2 = v2.magnitude()
```

## Normalize
### You can normalize a vector using the Vector.normalize() or ThDVector.normalize() method:

```
v1.normalize()
v2.normalize()
```

## Projection
### You can calculate the projection of one vector onto another using the Vector.projection() method:

```
v6 = vector.Vector(3, 4)
proj = v1.projection(v6)
```
# License
## This module is licensed under the MIT License. See LICENSE for more details.
