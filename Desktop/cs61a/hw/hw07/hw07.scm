(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cdr (cdr s)))
)



(define (sign num)
  (cond ((< num 0) -1)
        ((= num 0)  0)
        ((> num 0)  1)
  )
)


(define (square x) (* x x))

(define (pow x y)
        (cond ((= y 1) x)
              ((even? y) (square (pow x (/ y 2))))
              (else (* x (square (pow x (/ (- y 1) 2)))))
        )
)


(define (unique s)
  (if (null? s) s
      (cons (car s)
            (unique (filter (lambda (x) (not (equal? (car s) x))) (cdr s)
                    )
            )
      )
  )
)


(define (replicate x n)
        (define (rep-helper n list-so-far)
                (if (= n 0) (append list-so-far)
                    (rep-helper (- n 1) (cons x list-so-far))
                )
        )
        (rep-helper n nil)
)


(define (accumulate combiner start n term)
        (if (= n 0)
            start
            (combiner (term n) (accumulate combiner start (- n 1) term))
        )
)


#(define (accumulate-tail combiner start n term)
#        (define (helper n result)
#                (if (= n 0) result
#                    (helper (- n 1) (combiner (term n) result))
#                )
#        )
#        (helper n start)
#)

(define (accumulate-tail combiner start n term)
        (define (helper combiner start n term result)
                (if (= n 0) result
                    (helper combiner start (- n 1) term (combiner (term n) result))
                )
        )
        (helper combiner start n term start)
)

(define-macro (list-of map-expr for var in lst if filter-expr)
              (list 'begin list-of map-expr for var in lst if filter-expr)
)
