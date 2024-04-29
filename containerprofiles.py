class ContainerProfile:
  def __init__(self, name, height, width, depth):
    self.name = name
    self.height = height
    self.width = width
    self.depth = depth

a = ContainerProfile ('Record carton', 10, 15, 12)
b = ContainerProfile ('Document box-legal', 10.25, 5, 15.25)
c = ContainerProfile ('Document box-letter', 10.25, 5, 12.25)
d = ContainerProfile ('Document box-slim legal', 10.25, 2.5, 15.25)
e = ContainerProfile ('Document box-slim letter', 10.25, 2.5, 12.25)
f = ContainerProfile ('Document box-tall legal', 12.5, 5, 15.5)
g = ContainerProfile ('Document box-wide letter', 10.25, 7, 12.25)
h = ContainerProfile ('Document box-wide legal', 10.25, 7, 15.25)
i = ContainerProfile ('Flat box 1', 3, 12.5, 9.5)
j = ContainerProfile ('Flat box 2', 3, 13, 11)
k = ContainerProfile ('Flat box 3', 1.5, 11.5, 14.5)
l = ContainerProfile ('Flat box 4', 3, 11, 15)
m = ContainerProfile ('Flat box 5', 3, 11.5, 15)
n = ContainerProfile ('Flat box 6', 1.5, 11.5, 17.5)
o = ContainerProfile ('Flat box 7', 1.75, 15.25, 13.125)
p = ContainerProfile ('Flat box 8', 3.65, 15.75, 13.375)
q = ContainerProfile ('Flat box 9', 3, 18, 13)
r = ContainerProfile ('Flat box 10', 3, 14.5, 18.5)
s = ContainerProfile ('Flat box 11', 2, 22, 15)
t = ContainerProfile ('Flat box 12', 3.5, 20.5, 16.5)
u = ContainerProfile ('Flat box 13', 5, 20.5, 16.5)
v = ContainerProfile ('Flat box 14', 2.5, 25, 19)
w = ContainerProfile ('Flat box 15', 3, 16.5, 20.5)
x = ContainerProfile ('Flat box 16', 1.5, 18.5, 24.5)
y = ContainerProfile ('Flat box 17', 3, 17, 23)
z = ContainerProfile ('Flat box 18', 3, 20.5, 24.5)
aa = ContainerProfile ('Flat box 19', 3, 27.75, 21.875)
ab = ContainerProfile ('Flat box 20', 2.875, 30.875, 22.75)
ac = ContainerProfile ('Flat box 21', 3, 36, 24)
ad = ContainerProfile ('Flat box 22', 2.75, 16, 13)
ada= ContainerProfile ('Flat box 23', 2.875, 22.75, 30.875)
adb= ContainerProfile ('Flat box 24', 1.5, 22, 17)
ae = ContainerProfile ('Video cassette box', 4.875, 15.5, 15.5)
af = ContainerProfile ('Audio cassette box', 3, 12, 9)
afa = ContainerProfile ('Audiotape box', 1, 7.88, 7.88)
ag = ContainerProfile ('CD box 1', 5.875, 5.5, 12)
ah = ContainerProfile ('CD box 2', 5, 15, 6)
ai = ContainerProfile ('Negatives box 1', 5.5, 12, 7.5)
aj = ContainerProfile ('Negatives box 2', 5.5, 7.5, 12)
ak = ContainerProfile ('Negatives box 3', 4.5, 5.5, 12)
al = ContainerProfile ('Negatives box 4', 5.5, 4.5, 7.5)
ala = ContainerProfile ('Binder box', 4.12, 12.5, 13)
am = ContainerProfile ('Photo box 1', 5, 15.5, 12)
an = ContainerProfile ('Photo box 2', 5, 6.625, 4.625)
ao = ContainerProfile ('Microfilm box', 4.125, 4.125, 10.625)
ap = ContainerProfile ('Microfiche box', 4.5, 4, 6.25)
aq = ContainerProfile ('Storage box', 6, 7.375, 10.375)
ar = ContainerProfile ('Textile roll box 1', 4, 6, 36)
bs = ContainerProfile ('Textile roll box 2', 4, 6, 48)
at = ContainerProfile ('Textile roll box 3', 8, 10, 48)
au = ContainerProfile ('LP box 1', 13.25, 13.5, 3)
av = ContainerProfile ('LP box 2', 13, 13, 10.5)
aw = ContainerProfile ('Legacy box 1', 4.8, 5, 7)
ax = ContainerProfile ('Legacy box 2', 5, 7, 6.5)
ay = ContainerProfile ('Legacy box 3', 5, 7, 7)
az = ContainerProfile ('Legacy box 4', 4, 16, 24)
ba = ContainerProfile ('Legacy box 5', 3.5, 24.5, 32)
bb = ContainerProfile ('Legacy box 6', 3, 12, 25)
bc = ContainerProfile ('Legacy box 7', 5.5, 9, 16.75)

list = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, aa, ab, ac, ad, ada, adb, ae, af, afa, ag, ah, ai, aj, ak, al, ala, am, an, ao, ap, aq, ar, bs, at, au, av, aw, ax, ay, az, ba, bb, bc]

he = input('Height')
wi = input('Width')
de = input('Depth')

ExactList = []
AlmostList = []
SwitchExactList = []
SwitchAlmostList = []

#checks for exact matches and close matches in height
for x in list:
  if float(x.height) == float(he):
      ExactList.append(x.name)
  elif float(x.height) < (float(he) + 0.5) and float(x.height) > (float(he) - 0.5):
    AlmostList.append(x.name)

#updates exact match list for height and width
for x in list:
    if x.name in ExactList and float(x.width) != float(wi):
        AlmostList.append(x.name)
        ExactList.remove(x.name)

#updates almost match list for height and width
for x in list:
    if x.name in AlmostList:
        if float(x.width) > (float(wi) + 0.5):
            AlmostList.remove(x.name)
        elif float(x.width) < (float(wi) -0.5):
            AlmostList.remove(x.name)

#updates exact match list for height, width, and depth
for x in list:
    if x.name in ExactList and float(x.depth) != float(de):
        AlmostList.append(x.name)
        ExactList.remove(x.name)
        
#updates almost match list for height, width, and depth
for x in list:
    if x.name in AlmostList:
        if float(x.depth) > (float(de) + 0.5):
            AlmostList.remove(x.name)
        elif float(x.depth) < (float(de) -0.5):
            AlmostList.remove(x.name)
            
#checks for exact matches and close matches in height with width and depth switched
for x in list:
  if float(x.height) == float(he):
      SwitchExactList.append(x.name)
  elif float(x.height) < (float(he) + 0.5) and float(x.height) > (float(he) - 0.5):
    SwitchAlmostList.append(x.name)

#updates exact match list for height and width with width and depth switched
for x in list:
    if x.name in SwitchExactList and float(x.depth) != float(wi):
        SwitchAlmostList.append(x.name)
        SwitchExactList.remove(x.name)

#updates almost match list for height and width with width and depth switched
for x in list:
    if x.name in SwitchAlmostList:
        if float(x.depth) > (float(wi) + 0.5):
            SwitchAlmostList.remove(x.name)
        elif float(x.depth) < (float(wi) -0.5):
            SwitchAlmostList.remove(x.name)

#updates exact match list for height, width, and depth with width and depth switched
for x in list:
    if x.name in SwitchExactList and float(x.width) != float(de):
        SwitchAlmostList.append(x.name)
        SwitchExactList.remove(x.name)
        
#updates almost match list for height, width, and depth with width and depth switched
for x in list:
    if x.name in SwitchAlmostList:
        if float(x.width) > (float(de) + 0.5):
            SwitchAlmostList.remove(x.name)
        elif float(x.width) < (float(de) -0.5):
            SwitchAlmostList.remove(x.name)
for x in SwitchExactList:
    if x not in ExactList:
        ExactList.append(x)
        
for x in SwitchAlmostList:
    if x not in AlmostList:
        AlmostList.append(x)
            
if len(ExactList) > 0:
    print("I'm an exact match!")
    print(ExactList)
    exit()
else:
    print("Nothing matches exactly. :(")

if len(AlmostList) > 0:
    print("I'm pretty close!")
    print(AlmostList)
else:
    print("I've got nothing close for ya. :(")
