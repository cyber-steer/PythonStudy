import turtle as t

t.shape("turtle")
t.color("green")
t.speed(20)

# n = int(input("몇개? : "))
for i in range(100):
    t.circle(100)
    t.forward(20)
    t.forward(1)

t.done()