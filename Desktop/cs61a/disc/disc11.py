(define (reverse lst)
    (define (reverse_help lst lstsofar)
        (if (null? lst) lstsofar
            (reverse_help (cdr lst) (cons (car lst) lstsofar))
        )
    )
    (reverse_help lst nil)
)

# 6, 2 3 4 5 7
(define (insert n lst)
    (define (insert_helper n lst newlst)
        (cond   ((null? lst) (append newlst (list n)))
                ((< n (car lst)) (append newlst (list n) lst))
                (else (insert_helper n (cdr lst) (append newlst (list(car lst)))))
        )
    )
    (insert_helper n lst nil)
)


def make_lambda(params, body):
    """
    >>> f = make_lambda("x, y", "x + y")
    >>> f
    <function <lambda> at ...>
    >>> f(1, 2)
    3
    >>> g = make_lambda("a, b, c", "c if a > b else -c")
    >>> g(1, 2, 3)
    -3
    >>> make_lambda("f, x, y", "f(x, y)")(f, 1, 2)
    3
    """
    return eval("lambda " + params + ":" + body)


def make_lambda(params, body):
    return eval(f"lambda {params} : {body}")

(define-macro (or-macro expr1 expr2)
    `(let ((v1, expr1 ))
        (if v1 v1, expr2)
    )
)

(define-macro (prune-expr expr)
    (cons (car expr) (prune (cdr expr)))
)

(define-macro (when cond exprs)
    (list 'if cond (cons 'begin exprs) ''okay )
)

(define-macro (when cond exprs)
    `(if, cond, (cons 'begin exprs) 'okay')
)
