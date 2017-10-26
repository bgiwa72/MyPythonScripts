#!/usr/bin/python

#Strings
s = "Hello, world!"
print s
q = """This is my first python program"""
print q
e = ''
print e
print "-------------"
s2 = "spam's"
print s2

s4 = 'spam"s'
print s4

s5 = "s\tp\na\0m\nb\toy"
print s5
 
s6 = r"C:\new\test.spm"
print s6

x = "C:\\new\\test.dat"
print x

s7 = u'eggs\u0020spam'
print s7

s3 = r'\temp\spam'
print s3

print s+s2
print s3*3

print s2[2]
print s2[1:4]

print "Meaning " 'of' " Life"

f = "The length of s2 is\n" 
l = len(s2) 
#print f
#print l

print q.rstrip()
print s.replace('world', 'Africa')
print s.split(',')
print s.isdigit()
print s.lower()
print s.upper()

s8 = "knight\"s"
print s8

s9 = 'knight\'s'
print s9

print "================================"
x = 'a\nb\tc'
print x
xl = len(x)
print xl

h = 'ba'
print h
print len(h)

i = "b\ta"
print i
print len(i)

print "toronto\acity"
print "toronto\bcity"
print "toronto\fcity"
print "toronto\ncity"
print "toronto\rcity"
print "bash\rcity"
print "toronto,\tcity"
print "t\tcity"
print "toronto\vcity"


print "====================================="

#i=0
#for t in s
#   i+
#print i

#unicode
s = "hello"
u = u'hello'

print s
print u


#numbers
a = 1   #int
b = 1.0 #float
c = 1234567890987654321 #long

print a
print b
print c

#integer division
print 1/2
print 1.0/2
