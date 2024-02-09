(define (vir-fib n)
    (if (or (= n 1) (= n 0))
        n
        ((vir-fib (- n 1)) (vir-fib (- n 2)))
    )
)

(expect (vir-fib 10) 55)
(expect (vir-fib 1) 1)


(define (list-concat a b)
    (if (null? a)
        (if (null? b) 
            nil
            (cons (car a) (list-concat a (cdr b) )))
        (cons (car a) (list-concat (cdr a) b) )
    )
)

(expect (list-concat '(1 2 3) '(2 3 4)) (1 2 3 2 3 4))
(expect (list-concat '(3) '(2 1 0)) (3 2 1 0))


(define (map-fn fn lst)
    (if (null? lst)
        nil
        (cons (fn (car lst)) (map-fn fn (cdr lst))))
)

(map-fn (lambda (x) (* x x)) '(1 2 3))
; expect (1 4 9)


(define (remove item lst)
  (filter (lambda (x) (not (= x item))) lst)
)

(expect (remove 3 nil) ())
(expect (remove 2 '(1 3 2)) (1 3))
(expect (remove 1 '(1 3 2)) (3 2))
(expect (remove 42 '(1 3 2)) (1 3 2))
(expect (remove 3 '(1 3 3 7)) (1 7))


(define (duplicate lst)
    (if (null? lst)
        nil
        (cons (car lst) (cons (car lst) (duplicate (cdr lst))) ))
)

(expect (duplicate '(1 2 3)) (1 1 2 2 3 3))
(expect (duplicate '(1 1)) (1 1 1 1))
