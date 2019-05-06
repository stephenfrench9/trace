import datetime
u = str(datetime.datetime.utcnow()).split()[0]
reg = str(datetime.datetime.today()).split()[0]

print("utc: %s" % u)
print("doesn't work: %s" % reg)