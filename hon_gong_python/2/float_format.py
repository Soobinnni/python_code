# f를 활용한다.
# 형식 print("{:f}".format(실수))


# 부호
print("{:f}".format(52))
print("{:-f}".format(52))
print("{:-f}".format(-52))

print("{:20f}".format(52))
print("{:-20f}".format(-52))
print("{:-20f}".format(52))

print("{:020f}".format(52))
print("{:020f}".format(-52))

print("{:=20f}".format(52))
print("{:=20f}".format(-52))

print("{:=+20f}".format(52))
print("{:=+20f}".format(-52))

print("{:=+020f}".format(52))
print("{:=+020f}".format(-52))

print("{:20.5f}".format(52.5628624751))

print("{:=+020.4f}".format(52.5628624751))

# 52.000000
# 52.000000
# -52.000000
#            52.000000
#           -52.000000
#            52.000000
# 0000000000052.000000
# -000000000052.000000
#            52.000000
# -          52.000000
# +          52.000000
# -          52.000000
# +000000000052.000000
# -000000000052.000000
#             52.56286
# +0000000000052.56289