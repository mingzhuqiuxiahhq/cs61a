"""Q1"""
#a =  1 + 2 == 3
#b = 25
#28
# #t
# #f
"""Q2"""
#1
#10
#-96
#1
"""Q3"""
#(define (factorial x)
#        (cond (= x 1) (1)
#              (= x 0) (#f)
#         else (* x (factorial x-1)) )
#)

#(define (fib n)
#        (if (<= n 1) n
#        (+ (fib (- n 1)) (fib (- n 2)) )
#)
#)


"""Q4"""
#(define (my-append a b)
#        (if (null? a)
#        b
#        (conbs (car a) (my-append (cdr a) b)))
#)

#(define (insert element lst index)
#        (if (= index 0)
#        (cons element lst)
#        ( cons (car lst) (insert element (cdr lst) (- index 1))))
#)

#(define (dup lst)
#        (if (null? lst)
#        lst
#        (cons (car lst) (cons (car lst) (dup (cdr lst))))))
