(define (reverse lst)
    (if (or (null? lst) (null? (cdr lst)))
        lst
        (cons (reverse (cdr lst)) (car lst)))
)


; helper function
; returns the values of lst that are bigger than x
; e.g., (larger-values 3 '(1 2 3 4 5 1 2 3 4 5)) --> (4 5 4 5)
(define (larger-values x lst)
    (filter (lambda (a) (> a x)) lst))

(define (longest-increasing-subsequence lst)
    (if (null? lst)
        nil
        (begin
            (define first (car lst))
            (define rest (cdr lst))
            (define large-values-rest
                (larger-values first rest))
            (define with-first
                (cons first (longest-increasing-subsequence large-values-rest)))
            (define without-first
                (longest-increasing-subsequence large-values-rest))
            (if (> (length with-first) (length without-first))
                with-first
                without-first))))

(expect (longest-increasing-subsequence '()) ())
(expect (longest-increasing-subsequence '(1)) (1))
(expect (longest-increasing-subsequence '(1 2 3)) (1 2 3))
(expect (longest-increasing-subsequence '(1 9 2 3)) (1 2 3))
(expect (longest-increasing-subsequence '(1 9 8 7 6 5 4 3 2 3)) (1 2 3))
(expect (longest-increasing-subsequence '(1 9 8 7 2 3 6 5 4 5)) (1 2 3 4 5))
(expect (longest-increasing-subsequence '(1 2 3 4 9 3 4 1 10 5)) (1 2 3 4 9 10))


(define (cons-all first rests)
    (map (lambda (lst) (cons first lst)) rests)
)


;; List all ways to make change for TOTAL with DENOMS
(define (list-change total denoms)
    (cond 
        ((null? denoms)
            (()) ))
        ((< total (car denoms))
           (list-change total (cdr denoms)))
        (else (append 
                (cons-all (car denoms) (list-change (- total (car denoms)) denoms)) 
                (list-change total (cdr denoms))))
)
;scm> (list-change 10 '(25 10 5 1))
;((10) (5 5) (5 1 1 1 1 1) (1 1 1 1 1 1 1 1 1 1))
;scm> (list-change 5 '(4 3 2 1))
;((4 1) (3 2) (3 1 1) (2 2 1) (2 1 1 1) (1 1 1 1 1))